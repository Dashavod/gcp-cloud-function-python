from services.flowise import flowise_request
from services.openAI.openAI import openai_request
from services.rasa import rasa_request
from services.dialogflow import dialogflow_request
from services.stabledDiffusion import stable_diffusion_request


def reducer(body):
    print(body)
    if not body["message"]:
        return {"error": "Missing field 'message'"}
    engine = body["type"]
    match engine:
        case "flowise":
            return flowise_request(body["message"])
        case "gpt":
            return openai_request(body, body["sender"])
        case "rasa":
            return rasa_request(body["message"], body["sender"])
        case "dialogflow":
            return dialogflow_request(body["message"], body["sender"])
        case "stable_diffusion":
            return stable_diffusion_request(body["message"])
        case _:
            return {"error": "Incorrect type value, please change and try again"}
