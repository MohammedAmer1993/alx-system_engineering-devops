#!/usr/bin/python3
""" modlue is API for reddit"""

import requests
import json
import base64
from requests.auth import HTTPBasicAuth


def number_of_subscribers():
    client_id = "c2b98b7332474aadbe865e5f7cc9f605"
    client_sec = "2de8b0704b9942538da69bec3b0ac8fc"

    encode_string = client_id + ':' + client_sec
    encoded_auth = base64.b64encode(encode_string).decode('utf-8')
    headers = {
        "Authorization": f'Basic {encoded_auth}',
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    req = requests.post(
        "https://accounts.spotify.com/api/token", headers=headers, data=data, params=headers)

    # print(HTTPBasicAuth(client_id, client_sec))

    print(req.text)


number_of_subscribers()
