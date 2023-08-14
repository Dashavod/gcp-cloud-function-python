import json
import os
import requests
from dotenv import dotenv_values


def flowise_request(text):
    payload = {'question': text}

    url = os.getenv('FLOWISE_URL')
    headers = {"Authorization": f"Bearer {os.getenv('FLOWISE_API_KEY')}", "Content-Type": "application/json"}
    res = requests.post(url, headers=headers, json=payload)
    if res.status_code == 200:
        response_data = res.json()
        print(json.dumps(response_data, indent=2))  # Pretty print the JSON response
        return response_data
    else:
        print("Request failed with status code:", res.status_code)
        return None

