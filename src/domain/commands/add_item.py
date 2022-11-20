import infrastructure.storage

def execute(item):
    for i in item.split(','):
        infrastructure.storage.addJoker(i.strip())
