import requests, json
from ChattingBot.api.config import Authorization
from . import util, payload

def sendPush(url, user, msg):
    header = {"Content-Type": "application/json;charset=UTF-8", "Authorization": Authorization.key }
    requests.post(url=url, headers=header, data=json.dumps(payload.getPostPushMessage(user, msg)))

def upLoad(url):
    header = {"Content-Type": "application/json;charset=UTF-8", "Authorization": Authorization.key }
    requests.post(url=util.UPDATE_URL, headers=header, data=json.dumps(payload.getUpdateBox(url)))

def sendIMAG(user, URL):
    header = {"Content-Type": "application/json;charset=UTF-8", "Authorization": Authorization.key }
    requests.post(url=util.PUSH_URL, headers=header, data=json.dumps(payload.getImageBox(user, URL)))
