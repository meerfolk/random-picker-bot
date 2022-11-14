# type: ignore
import redis
import os

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PREFIX = 'picking_daily_anekdot:'

r = redis.Redis(host=REDIS_HOST, port=6379, db=0)

def __getFullJokersSetKey():
    return f'{REDIS_PREFIX}jokers:list:full'

def __getNextJokersSetKey():
    return f'{REDIS_PREFIX}jokers:list:next'

def __getSet(key):
    listMap = map(bytes.decode, r.smembers(key))

    return list(listMap)

def __getSetSize(key):
    return r.scard(key)

def __restoreJokersSet():
    r.copy(__getFullJokersSetKey(), __getNextJokersSetKey(), replace=True)

def getFullList():
    return __getSet(__getFullJokersSetKey())

def getNetxtJokersList():
    return __getSet(__getNextJokersSetKey())

def getNextJoker():
    nextJoker: bytes = r.spop(__getNextJokersSetKey())

    if __getSetSize(__getNextJokersSetKey()) == 0:
        __restoreJokersSet()

    return nextJoker.decode()

def addJoker(joker):
    r.sadd(__getFullJokersSetKey(), joker)
    r.sadd(__getNextJokersSetKey(), joker)
