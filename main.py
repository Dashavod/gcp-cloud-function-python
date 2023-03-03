from jsonToStorage import jsonToStore
from kernel import kernel
import requests
import os
from dialogflow import detect_intent_texts
from stableDiffusion import stableDiffusion
from templates import template_basic
import functions_framework
from firestore import *


@functions_framework.http
def root(request):
    data = request.get_json()
    print(data)
    text = data["message"]
    user = data["sender"]
    engine = data["type"]

    if engine == "gpt":
        response = kernel(f"{template_basic} \n provide information about {text} in the same format as above", user,
                          0.27)
        try:
            res = eval(response)
        except Exception as e:
            print(e)
            return f"OpenAI provide information with wrong stucture, please retry\n {e}"

        id = add_document_to_firestore(res)
        document = find_document_in_firestore_by_id(id)
        return document

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
        return response

    return {"message": "Incorrect type value, please change and try again"}
