
import os
from services import service
import functions_framework
from dotenv import dotenv_values

@functions_framework.http
def root(request):
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)

        # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }


    if request is None: return "empty body"
    body = request.get_json()
    key = os.getenv('KEY') if os.getenv('KEY') else dotenv_values("env/.env")[
        'KEY']

    if body["key"] != key: return ("Unautorized",401)
    response = service.reducer(body)
    return (response, 200, headers)