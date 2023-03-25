# -*- coding: utf-8 -*-
__author__ = "C418____11 <553515788@qq.com>"
__version__ = "0.0.1"

from abc import ABC
import functools
from javascript import require

mineflayer = require("mineflayer", "latest")


class Plugin(ABC):

    def reloader(self): ...

    def enable(self): ...

    def disable(self): ...


class Bot:

    def __init__(self, init_arg: dict, **_):

        self.init_arg = init_arg  # 创建机器人的参数
        self.ons = set()  # 在机器人重置时需重新加载On
        self.plugins = {}  # 需加载的插件库

        self.bot = mineflayer.createBot(init_arg)  # 创建机器人

    def chat(self, msg=''):
        return self.bot["chat"](msg)  # chat方法重写

    def quit(self, reason=''):
        return self.bot["quit"](reason)  # quit方法重写

    def on(self, event, fn):  # on外部钩子重写
        self.bot.on(event, fn)

    def load_plugin(self, raw_plugin, plugin: Plugin):  # 加载插件重写
        self.bot.loadPlugin(raw_plugin)  # 加载插件

        try:
            self.plugins[raw_plugin]
        except KeyError:
            raise KeyError(f"The plugin <{raw_plugin}> already exists")
        else:
            self.plugins[raw_plugin] = plugin

        plugin.reloader()

    def _re_load_on(self):  # 在机器人重置时重新加载on钩子
        for event, func in self.ons:
            self.on(event, func)

    def _re_load_plugin(self):  # 在机器人重置时重新加载插件
        for plugin, raw_plugin in self.plugins:
            self.bot.loadPlugin(raw_plugin)
            plugin.reloader()

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


def main():
    pass


if __name__ == '__main__':
    main()
