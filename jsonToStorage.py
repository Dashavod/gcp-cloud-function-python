import datetime
from datetime import timedelta

from flask import send_file
from huggingface_hub.inference_api import InferenceApi
import os
from io import StringIO, BytesIO
import json
import requests
import firebase_admin
from firebase_admin import storage
from requests import ReadTimeout
from dotenv import dotenv_values

cred_obj = firebase_admin.credentials.Certificate('cred.json')
def jsonToStore(company: dict):
    exp = timedelta(hours=3)
    bucket = storage.bucket()
    blob_new = bucket.blob(f"{company['site']}-{str(datetime.datetime.now())}")
    blob_new.upload_from_string(json.dumps(company,indent=4), content_type="application/json")
    blob_url = blob_new.generate_signed_url(expiration=exp)
    return blob_url
