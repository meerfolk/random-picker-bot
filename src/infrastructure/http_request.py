import requests

def get(url):
    response = requests.get(url)

    json = response.json()

    return json
