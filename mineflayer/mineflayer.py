# -*- coding: utf-8 -*-
__author__ = "C418____11 <553515788@qq.com>"

import weakref
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

    @property
    def username(self):
        return self.bot["username"]


class Plugin(ABC):
    raw: javascript.proxy.Proxy

    def __eq_options__(self, other_bot: ABCBot) -> bool: ...

    def reloader(self, bot: ABCBot) -> None: ...

    def enable(self) -> None: ...

    def disable(self) -> None: ...

    def __hash__(self) -> int: ...

    def __eq__(self, other) -> bool: ...


class Bot(ABCBot):
    bot_dict = weakref.WeakValueDictionary()

    def __init__(self, init_arg: dict):
        super().__init__(init_arg)

        self.ons = set()  # 在机器人重置时需重新加载On
        self.plugins = set()  # 需加载的插件库

    def reg_bot(self):
        cls = type(self)
        if self.username is None:
            raise AttributeError("self.username mustn't be None")
        cls.bot_dict[self.username] = self

    def on(self, event, fn):  # on外部钩子重写
        wrapper_fn = functools.partial(self.on_wrapper, fn)
        self.bot.on(event, wrapper_fn)

    def get_plugin(self, plugin: Plugin) -> Plugin:
        return (self.plugins & {plugin}).pop()

    def load_plugin(self, plugin: Plugin) -> None:  # 加载插件重写
        self.bot.loadPlugin(plugin.raw["plugin"])  # 加载插件

        try:
            if self.get_plugin(plugin).__eq_options__(self):
                raise KeyError(f"The plugin <{plugin.raw}> already exists")
        except KeyError:
            pass

        self.plugins.add(plugin)

        plugin.reloader(self)

    def _re_load_on(self) -> None:  # 在机器人重置时重新加载on钩子
        for event, func in self.ons:
            self.on(event, func)

    def _re_load_plugin(self) -> None:  # 在机器人重置时重新加载插件
        for plugin in self.plugins:
            self.load_plugin(plugin)

    def reconnect(self) -> None:  # 重置机器人
        self.bot = mineflayer.createBot(self.init_arg)
        self._re_load_on()
        self._re_load_plugin()

    def on_wrapper(self, fn, *args, **kwargs):
        fn(self, *args[1:], **kwargs)


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
