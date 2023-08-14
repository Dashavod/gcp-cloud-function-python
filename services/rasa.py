import os
import requests


def rasa_request(text, user):
    payload = {'message': text, 'sender': user}

    url = os.getenv('RASA_URL')
    res = requests.post(url, json=payload)
    print(res.json())
    return res.text
