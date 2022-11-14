import infrastructure.http_request as http_request
import os

token = os.environ['TOKEN']
botName = os.environ['BOT_NAME']

def getUrl(method):
    return f'https://api.telegram.org/bot{token}/{method}'

def getMessages(offset: int = 0):
    url = getUrl('getUpdates')

    response = http_request.get(f'{url}?offset={offset}&limit=100&timeout=10')

    if response['ok']:
        return response['result']

    return []

def getChatAdministrators(chatId):
    url = getUrl('getChatAdministrators')

    response = http_request.get(f'{url}?chat_id={chatId}')

    if response['ok']:
        return response['result']

    return []

def replyToMessage(chatId, messageId, text):
    url = getUrl('sendMessage')

    http_request.get(f'{url}?chat_id={chatId}&text={text}&reply_to_message_id={messageId}')

def isMessageToBot(text):
    return text.startswith(f'@{botName}')

def isMessageFromAdmin(chatId, userId):
    administators = getChatAdministrators(chatId)

    for admin in administators:
        if admin['user']['id'] == userId:
            return True

    return False

def trimBotName(text):
    return text.replace(f'@{botName} ', '')
