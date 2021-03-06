# ripple!api
# https://docs.ripple.moe/docs

import requests
import re
import json

with open("/home/aiae/r/config.json", "r") as f: 
    config = json.load(f)

def user(id=None, name=None):
    try:
        request = requests.get("https://ripple.moe/api/v1/users/full", params={"name" : name, "id" : id}, headers={'token': config["ripple_token"]})
    except requests.exceptions.RequestException as e:
        return
    return json.loads(request.text)

def recent(id=None, name=None, mode=0, limit=1):
    try:
        request = requests.get("https://ripple.moe/api/v1/users/scores/recent", params={"id" : id, "mode" : mode, "l" : limit}, headers={'token': config["ripple_token"]})
    except requests.exceptions.RequestException as e:
        return
    return json.loads(request.text)

def isonline(id=None, name=None):
    try:
        request = requests.get("http://c.ripple.moe/api/v1/isOnline", params={"id" : id}, headers={'token': config["ripple_token"]})
    except requests.exceptions.RequestException as e:
        request = requests.get("http://c.ripple.moe/api/v1/isOnline", params={"id" : id}, headers={'token': config["ripple_token"]})
    return json.loads(request.text)