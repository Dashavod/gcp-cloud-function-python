

from jsonToStorage import jsonToStore
from kernel import kernel
import requests
import os
from dialogflow import detect_intent_texts
from stableDiffusion import stableDiffusion
from templates import template_basic
import functions_framework

@functions_framework.http
def root(request):

    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Authorization, Content-Type',
            'Access-Control-Allow-Credentials': 'true'
        }

        return ('', 204, headers)
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': 'true'
    }

    data = request.get_json()
    print(data)
    text = data["message"]
    user = data["sender"]
    engine = data["type"]
    if engine == "gpt":
        response = kernel(f"{template_basic} \n provide information about {text} in the same format as above", "123456", 0.27)
        res =eval(response)
        res["url"] = jsonToStore(res)
        return (res, 200, headers)
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
