from aihub.dialogflow import detect_intent_texts


def dialogflow_request(text,user):
    response = detect_intent_texts("devtorium-bot-e9vy", user, {text}, "en")
    return {"message": response}