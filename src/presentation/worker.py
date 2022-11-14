from domain import bot, message

def main():
    offset = 0

    while True:
        messages = bot.getMessages(offset + 1)

        offset = message.getOffset(messages)

        message.handleMessages(messages)

main()
