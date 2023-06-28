# -*- coding: utf-8 -*-
__author__ = "C418____11 <553515788@qq.com>"

from mineflayer.mineflayer import ABCBot, Plugin
from javascript import require

auto_eat = require('mineflayer-auto-eat')


class AutoEat(Plugin):

    raw = auto_eat

    def __init__(self, options: dict):
        self._bot = None

        self.autoEat_options = options

    def reloader(self, bot: ABCBot):
        self._bot = bot
        bot.autoEat = self  # 从外部为类添加属性
        bot.bot.autoEat.options = self.autoEat_options  # 重新加载属性

    def enable(self):  # 启用插件
        self._bot.bot.autoEat.enable()

    def disable(self):  # 禁用插件
        self._bot.bot.autoEat.disable()

    def __eq_options__(self, other: ABCBot):
        return self._bot.bot.autoEat.options == other.bot.autoEat.options

    def __eq__(self, other):
        return id(auto_eat) == id(other)

    def __hash__(self):
        return id(auto_eat)


def main():
    pass


if __name__ == '__main__':
    main()
