# Mineflayer-encapsulated-in-Python

用python封装的mineflayer

    import sys
    import time

    from mineflayer.mineflayer import Bot, On

    bot = Bot({
        "username": "bot",
        "host": "127.0.0.1",
        "port": 25565,
        "version": "1.16.5",
        "keepAlive": True,
    })


    @On(bot, "login")
    def on_login(self: Bot):
        self.chat("Login!")


    @On(bot, "kicked")
    @On(bot, "error")
    def on_quit(_, *reason):
        print(f"quit! reason: ", end='')
        print(reason, file=sys.stderr)
        time.sleep(2)
        bot.reconnect()
    
    
    @On(bot, "message")
    def on_message(self: Bot, *_):
        print(f"Recv message! details: ", end='')
        print(_)
    
    
    def main():
        while True:
            pass
        pass
    
    
    if __name__ == "__main__":
        main()

------------------------------------------------------------------
游戏内消息

    bot加入了游戏
    <bot> Login!
    <C418____11> test
    <C418____11> /kick bot test
    已踢出bot
    bot退出了游戏
    bot加入了游戏
    <bot> Login!

-----------------------------------------------------------------
控制台消息

    Recv message! details: (ChatMessage {
      json: { translate: 'chat.type.text', with: [ [Object], 'Login!' ] },
      translate: 'chat.type.text',
      with: [
        ChatMessage {
          json: [Object],
          text: 'bot',
          bold: undefined,
          italic: undefined,
          underlined: undefined,
          strikethrough: undefined,
          obfuscated: undefined,
          color: undefined,
          clickEvent: [Object],
          hoverEvent: [Object]
        },
        ChatMessage {
          json: [MessageBuilder],
          text: 'Login!',
          extra: [],
          bold: undefined,
          italic: undefined,
          underlined: undefined,
          strikethrough: undefined,
          obfuscated: undefined,
          color: undefined
        }
      ],
      bold: undefined,
      italic: undefined,
      underlined: undefined,
      strikethrough: undefined,
      obfuscated: undefined,
      color: undefined
    }, 'chat', '67128b5b-2e6b-3ad1-baa0-1b937b03e5c5', None)
    
    Recv message! details: (ChatMessage {
      json: { translate: 'chat.type.text', with: [ [Object], 'test' ] },
      translate: 'chat.type.text',
      with: [
        ChatMessage {
          json: [Object],
          text: 'C418____11',
          bold: undefined,
          italic: undefined,
          underlined: undefined,
          strikethrough: undefined,
          obfuscated: undefined,
          color: undefined,
          clickEvent: [Object],
          hoverEvent: [Object]
        },
        ChatMessage {
          json: [MessageBuilder],
          text: 'test',
          extra: [],
          bold: undefined,
          italic: undefined,
          underlined: undefined,
          strikethrough: undefined,
          obfuscated: undefined,
          color: undefined
        }
      ],
      bold: undefined,
      italic: undefined,
      underlined: undefined,
      strikethrough: undefined,
      obfuscated: undefined,
      color: undefined
    }, 'chat', '13cf9efc-375b-4ccb-90eb-28aad7b24532', None)
    ('{"text":"test"}', True)
    
    quit! reason: Recv message! details: (ChatMessage {
      json: { translate: 'chat.type.text', with: [ [Object], 'Login!' ] },
      translate: 'chat.type.text',
      with: [
        ChatMessage {
          json: [Object],
          text: 'bot',
          bold: undefined,
          italic: undefined,
          underlined: undefined,
          strikethrough: undefined,
          obfuscated: undefined,
          color: undefined,
          clickEvent: [Object],
          hoverEvent: [Object]
        },
        ChatMessage {
          json: [MessageBuilder],
          text: 'Login!',
          extra: [],
          bold: undefined,
          italic: undefined,
          underlined: undefined,
          strikethrough: undefined,
          obfuscated: undefined,
          color: undefined
        }
      ],
      bold: undefined,
      italic: undefined,
      underlined: undefined,
      strikethrough: undefined,
      obfuscated: undefined,
      color: undefined
    }, 'chat', '67128b5b-2e6b-3ad1-baa0-1b937b03e5c5', None)
    ('{"text":"test"}', True)
    
    Recv message! details: (ChatMessage {
      json: { translate: 'chat.type.text', with: [ [Object], 'Login!' ] },
      translate: 'chat.type.text',
      with: [
        ChatMessage {
          json: [Object],
          text: 'bot',
          bold: undefined,
          italic: undefined,
          underlined: undefined,
          strikethrough: undefined,
          obfuscated: undefined,
          color: undefined,
          clickEvent: [Object],
          hoverEvent: [Object]
        },
        ChatMessage {
          json: [MessageBuilder],
          text: 'Login!',
          extra: [],
          bold: undefined,
          italic: undefined,
          underlined: undefined,
          strikethrough: undefined,
          obfuscated: undefined,
          color: undefined
        }
      ],
      bold: undefined,
      italic: undefined,
      underlined: undefined,
      strikethrough: undefined,
      obfuscated: undefined,
      color: undefined
    }, 'chat', '67128b5b-2e6b-3ad1-baa0-1b937b03e5c5', None)
