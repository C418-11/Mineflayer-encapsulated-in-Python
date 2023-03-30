# -*- coding: utf-8 -*-
__author__ = "C418____11 <553515788@qq.com>"

from abc import ABC
import functools

import javascript.proxy
from javascript import require

mineflayer = require("mineflayer", "latest")


class ABCBot(ABC):
    def __init__(self, init_arg: dict):
        self.init_arg = init_arg

        self.bot = mineflayer.createBot(init_arg)

    def chat(self, msg=''):
        return self.bot["chat"](msg)  # chat方法重写

    def quit(self, reason=''):
        return self.bot["quit"](reason)  # quit方法重写


class Plugin(ABC):
    raw: javascript.proxy.Proxy

    def __eq_options__(self, other_bot: ABCBot) -> bool: ...

    def reloader(self, bot: ABCBot) -> None: ...

    def enable(self) -> None: ...

    def disable(self) -> None: ...


class Bot(ABCBot):

    def __init__(self, init_arg: dict):
        super().__init__(init_arg)

        self.ons = set()  # 在机器人重置时需重新加载On
        self.plugins = set()  # 需加载的插件库

    def on(self, event, fn):  # on外部钩子重写
        self.bot.on(event, fn)

    def load_plugin(self, plugin: Plugin):  # 加载插件重写
        self.bot.loadPlugin(plugin.raw)  # 加载插件

        if plugin in self.plugins:
            if not plugin.__eq_options__((self.plugins & {plugin}).pop()):
                raise KeyError(f"The plugin <{plugin.raw}> already exists")

        self.plugins.add(plugin)

        plugin.reloader(self)

    def _re_load_on(self):  # 在机器人重置时重新加载on钩子
        for event, func in self.ons:
            self.on(event, func)

    def _re_load_plugin(self):  # 在机器人重置时重新加载插件
        for plugin in self.plugins:
            self.load_plugin(plugin)

    def reconnect(self):  # 重置机器人
        self.bot = mineflayer.createBot(self.init_arg)
        self._re_load_on()
        self._re_load_plugin()


def On(bot: Bot, event):  # On装饰器重写
    def decorator(_fn):
        bot.on(event, _fn)
        bot.ons.add((event, _fn))

        @functools.wraps(_fn)
        def wrapper(*args, **kwargs):
            _fn(*args, **kwargs)

        return wrapper

    return decorator


def createBot(init_arg: dict) -> Bot:
    return Bot(init_arg)


def main():
    pass


if __name__ == '__main__':
    main()
