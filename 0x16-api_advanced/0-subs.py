#!/usr/bin/python3
""" Number of subscribers for an reddit user """

import requests
import json
import uuid

CLIENT_ID = "BZbNK5UKZmIWH6Z_uTin3g"
RESPONSE_TYPE = "token"
STATE = str(uuid.uuid4())
REDIRECT_URI = "https://www.google.com"
SCOPE = "read"


def number_of_subscribers(subreddit):
    """ function to return number of subscribers of reddit user
    Args: 
        subreddit (string): the name of reddit user
    Return: 
        int : number of subscribers
        0   : invalid reddit user
    """
    url = "https://www.reddit.com/api/v1/authorize"
    payload = {"client_id": CLIENT_ID, "response_type": RESPONSE_TYPE,
               "state": STATE, "redirect_uri": REDIRECT_URI, "scope": SCOPE}

    r = requests.get(url, params=payload)
    return r


r = number_of_subscribers("programming")
print(r.status_code)
print(r.json())
