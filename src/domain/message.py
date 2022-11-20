from functools import reduce

from domain import bot
from infrastructure import storage
from domain.commands import add_item

def __getNextJokerMessage(joker, nextJokers):
    return f'''
        Следующий: {joker}
        После этого будет один из следующих: {nextJokers}
    '''

def addJoker(command: str):
    joker = command.split(' ', 1)[1]

    add_item.execute(joker)

    return joker

def handleMessages(messages):
    for message in messages:
        if not 'message' in message:
            continue

        if not 'text' in message['message']:
            continue

        text: str = message['message']['text']

        if not bot.isMessageToBot(text):
            continue

        chatId: str = message['message']['chat']['id']
        messageId: str = message['message']['message_id']

        if not bot.isMessageFromAdmin(chatId, message['message']['from']['id']):
            continue

        command: str = bot.trimBotName(text)

        if command.startswith('Добавить'):
            joker =  addJoker(command)
            bot.replyToMessage(chatId, messageId, f'{joker} добавлен')
            continue

        if command.startswith('Список'):
            jokers = storage.getFullList()
            bot.replyToMessage(chatId, messageId, f'Список: {jokers}')
            continue

        if command.startswith('Следующий'):
            joker = storage.getNextJoker()
            nextJokers = storage.getNetxtJokersList()
            bot.replyToMessage(chatId, messageId, __getNextJokerMessage(joker, nextJokers))
            continue



def getOffset(messages):
    return reduce(lambda acc, message: max(acc, message['update_id']), messages, 0)
