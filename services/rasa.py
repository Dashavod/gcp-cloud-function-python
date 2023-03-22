import os

import requests
from dotenv import dotenv_values

def rasa_request(text,user):
    payload = {'message': text, 'sender': user}
    openai_api_key = os.getenv('OPENAI_API_TOKEN') if os.getenv('OPENAI_API_TOKEN') else dotenv_values("./env/.env")[
        'OPENAI_API_TOKEN']
    # res = await task(payload)
    url = os.getenv('RASA_URL')
    res = requests.post(url, json=payload)
    print(res.json())
    return res.text