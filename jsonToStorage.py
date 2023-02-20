import datetime
from datetime import timedelta
import json
from firebase_admin import storage

#cred_obj = firebase_admin.credentials.Certificate('cred.json')
def jsonToStore(company: dict):
    exp = timedelta(hours=3)
    storage_client = storage.Client(project="devtorium-qna")
    bucket = storage_client.get_bucket("gcf-sources-334279855271-europe-west3")
    blob_new = bucket.blob(f"{company['site']}-{str(datetime.datetime.now())}")
    blob_new.upload_from_string(json.dumps(company,indent=4), content_type="application/json")
    blob_url = blob_new.generate_signed_url(expiration=exp)
    return blob_url
