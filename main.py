from kernel import kernel
import requests
import os
from dialogflow import detect_intent_texts

URL = os.getenv('RASA_URL')


def root(request):
    data = request.get_json()
    print(data)
    text = data["message"]
    user = data["sender"]
    engine = data["type"]
    if engine == "gpt":
        response = kernel(text, user, 0)
        return {"message": response}
    if engine == "rasa":

            payload = {'message': text, 'sender': user}  # res = await task(payload)
            res = requests.post("http://192.168.0.174:5005/webhooks/rest/webhook", json=payload)
            print(res.json())
            return res.text
    if engine == "dialogflow":
        response = detect_intent_texts("devtorium-bot-e9vy", user, {text}, "en")
        return {"message": response}


    return {"message": "Incorrect type value, please change and try again"}
