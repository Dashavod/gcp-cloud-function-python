
import os
import json
import requests
from dotenv import dotenv_values

def stableDiffusion(prompt: str):

    api_token = os.getenv('RUNWAYML_API_TOKEN') if os.getenv('RUNWAYML_API_TOKEN') else dotenv_values("env/.env")[
        'RUNWAYML_API_TOKEN']

    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {api_token}"}

    data = json.dumps(prompt)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    # inference = InferenceApi(repo_id="runwayml/stable-diffusion-v1-5", token=api_token)
    # img = inference(inputs=prompt)
    # print(img)
    # # img.save("images/img2.png", format='JPEG', quality=75)
    # imageToStore(response.content)
    return response
