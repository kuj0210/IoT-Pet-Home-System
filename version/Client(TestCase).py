#-*-coding: utf-8-*-

import json
import requests

SERVER = "127.0.0.1"
PORT = 8080

def attachSendProtocol(message):
    param = {'user_key':'test', 'content':message, 'type':'text'}
    #url = 'http://ec2-13-125-111-212.ap-northeast-2.compute.amazonaws.com:8080/message'
    url = "http://localhost:8080/message"
    header={'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(url=url, headers = header, data=json.dumps(param))
    return response

def recvFromServer(response):
    data = response.json()
    message = data['message']['text']
    print("Server << " + message)
    return message

while True:
    message = input("User >> ")
    response = attachSendProtocol(message)
    recvFromServer(response)
