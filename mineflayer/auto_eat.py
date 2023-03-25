# -*- coding: utf-8 -*-
__author__ = "C418____11 <553515788@qq.com>"
__version__ = "0.0.1"

from mineflayer.mineflayer import Bot, Plugin
from javascript import require

auto_eat = require('mineflayer-auto-eat', "latest")


class AutoEat(Plugin):
    def __init__(self, bot: Bot, options: dict):
        self.bot = bot
        self.bot.load_plugin(auto_eat, self)

        self.autoEat_options = options
        self.reloader()

    def set_options(self, options: dict):
        self.autoEat_options = options
        self.reloader()

    def reloader(self, bot: Bot = None):
        bot.autoEat = self  # 从外部为类添加属性
        self.bot = bot  # 重置储存的bot
        if bot is not None:
            self.bot.bot.autoEat.options = self.autoEat_options  # 重新加载属性

    def enable(self):  # 启用插件
        self.bot.bot.autoEat.enable()

    def disable(self):  # 禁用插件
        self.bot.bot.autoEat.disable()


def main():
    pass


if __name__ == '__main__':
    main()
