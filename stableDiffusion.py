import datetime
from datetime import timedelta

from flask import send_file
import os
from io import BytesIO
import json
import requests
#import firebase_admin
#from google.cloud import storage
from requests import ReadTimeout

#cred_obj = firebase_admin.credentials.Certificate('cred.json')
#default_app = firebase_admin.initialize_app(options={"storageBucket": "gcf-sources-334279855271-europe-west3"})

def stableDiffusion(prompt: str):

    api_token = os.getenv('RUNWAYML_API_TOKEN')
    API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
    headers = {"Authorization": f"Bearer {api_token}"}

    data = json.dumps(prompt)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    # inference = InferenceApi(repo_id="runwayml/stable-diffusion-v1-5", token=api_token)
    # img = inference(inputs=prompt)
    # print(img)
    # # img.save("images/img2.png", format='JPEG', quality=75)
    # imageToStore(response.content)
    try:
        return response.content #{"image_url": imageToStore(response.content)}
    except ReadTimeout:
        return "stable diffusion doesn't return image"


def serve_pil_image(pil_img):

    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=75)
    img_io.seek(0)
    #imageToStore(pil_img)
    return send_file(img_io, mimetype='image/jpeg')

# def imageToStore(res):
#     exp = timedelta(hours=3)
#     # bucket = storage.bucket()
#     storage_client = storage.Client(project="devtorium-qna")
#     bucket = storage_client.get_bucket("gcf-sources-334279855271-europe-west3")
#
#     blob_new = bucket.blob(str(datetime.datetime.now()))
#     blob_new.upload_from_string(res, content_type="image/jpeg")
#
#     blob_url = blob_new.generate_signed_url(expiration=exp)
#     return blob_url


    #blob.download_to_filename("/images/test.png")
