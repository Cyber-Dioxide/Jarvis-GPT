import requests
import json

def advise():
    url = 'https://api.adviceslip.com/advice'

    req = requests.get(url).content.decode()

    return (json.loads(req)['slip']['advice'])

