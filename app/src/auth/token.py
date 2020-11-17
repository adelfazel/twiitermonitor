#!/usr/bin/env python3

import base64
import requests
import urllib.parse

OAUTH2_TOKEN = 'https://api.twitter.com/oauth2/token'


class Authenticator:
    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret

    def get_bearer_token(self):
        try:
            consumer_key = urllib.parse.quote(self.consumer_key)
            consumer_secret = urllib.parse.quote(self.consumer_secret)
            bearer_token = f"{consumer_key}:{consumer_secret}"
            base64_encoded_bearer_token = base64.b64encode(bearer_token.encode('utf-8'))
            headers = {
                "Authorization": f"Basic {base64_encoded_bearer_token.decode('utf-8')}",
                "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
                "Content-Length": "29"}
            response = requests.post(OAUTH2_TOKEN, headers=headers, data={'grant_type': 'client_credentials'}).json()
            print(f"Successfully Obtained bearer token")
            return f"{response['token_type']} {response['access_token']}"
        except Exception as E:
            print(f"unable to obtain auth param due to {E}")
            raise
