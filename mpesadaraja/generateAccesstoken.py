from requests.auth import HTTPBasicAuth
import requests
from django.http import JsonResponse

def get_access_token():
    consumer_key = 'appjpPyYXD0c4KENbeU5Fj6MHkREuvpb'
    consumer_secret = '6ZHnCEHFgl05mj3h'
    access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    headers = {'Content-Type': 'application/json'}
    response = requests.get(access_token_url, headers=headers, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    response.raise_for_status() 
    result = response.json()
    access_token = result.get('access_token', '')
    return access_token


