from flask import send_file
from huggingface_hub.inference_api import InferenceApi
import os
from PIL import Image
from io import StringIO, BytesIO

import json
import requests

def stableDiffusion(prompt: str):

    api_token = "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"
    print(api_token)
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {api_token}"}

    data = json.dumps(prompt)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    # inference = InferenceApi(repo_id="runwayml/stable-diffusion-v1-5", token=api_token)
    # img = inference(inputs=prompt)
    # print(img)
    # # img.save("images/img2.png", format='JPEG', quality=75)
    img = Image.open(BytesIO(response.content))
    return serve_pil_image(img)

def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=75)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')