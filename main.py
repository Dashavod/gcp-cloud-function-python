import json

from dotenv import dotenv_values

from jsonToStorage import jsonToStore
from kernel import kernel
import requests
import os
from dialogflow import detect_intent_texts
from stableDiffusion import stableDiffusion
from templates import template_basic


def root(request):
    data = request.get_json()
    print(data)
    text = data["message"]
    user = data["sender"]
    engine = data["type"]
    if engine == "gpt":
        response = kernel(f"{template_basic} \n provide information about {text} in the same format as above", "123456", 0.27)
        res =eval(response)
        res["url"] = jsonToStore(res)
        return res
    if engine == "rasa":

            payload = {'message': text, 'sender': user}  # res = await task(payload)
            res = requests.post(os.getenv('RASA_URL'), json=payload)
            print(res.json())
            return res.text
    if engine == "dialogflow":
        response = detect_intent_texts("devtorium-bot-e9vy", user, {text}, "en")
        return {"message": response}
    if engine == "stable_diffusion":
        response = stableDiffusion(text)
        return  response

    return {"message": "Incorrect type value, please change and try again"}
