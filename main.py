


def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json(force=True, silent=True, cache=True)  # see https://flask.palletsprojects.com/en/2.0.x/api/ get_json Parse data as JSON
    #in v.2.1 of the Flask framework they changed the impl of the get_json and if the content type if not provided it returns http 400 - BAD Requests, therefore we are usong now force=true and silent=true

    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'


import json
from kernel import kernel
import aiohttp
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
        print("1")
        response = detect_intent_texts("devtorium-bot-e9vy", "123456", {text}, "en")
        return {"message": response}




    return {"message": "Incorrect type value, please change and try again"}
