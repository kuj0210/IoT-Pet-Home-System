import requests
import json
from flask import jsonify


class Translator():
    userList = []
    SERIAL=""
    Name=""
    Count =0

    def __init__(self):
        # URL 관리
        self.SERVER_URL = "https://kit-iot-system.tk/"
        self.PUSH_URL = self.SERVER_URL+"push"
        self.BOOT_URL = self.SERVER_URL + "bootUp"
        self.RQST_URL = self.SERVER_URL + "RQST"

        #헤더
        self.Send_Header = {"Content-Type": "application/json;charset=UTF-8", "Authorization": "MOBILE _YSTEM"}

    def getIMAG_URL(self,user):
        return self.SERVER_URL+user+"/image"

    def getPostBodyMessage(self,user,text):
        postBodyMessage = {
            "event": "send",
            "user" : user,
            "textContent": {
                "text": text
            },
            "options": {
                "notification": "true"
            }
        }
        return postBodyMessage

    def sendMsg(self,url,user,msg):
        res = requests.post(url=url, headers=self.Send_Header, data=json.dumps(self.getPostBodyMessage(user,msg)))
        return str(res.__dict__['_content'], encoding='utf-8')

    def pushToUser(self,user,msg):
        self.sendMsg(self.PUSH_URL,user,msg)

    def pushToAllUser(self,msg):
        #print("전유저푸쉬")
        for user in Translator.userList:
            self.pushToUser(user,msg)

    def pushImage(self, user, path):
        print(user)
        print(path)
        #files = open(path, 'rb')
        files = open(path, 'rb')
        print("오픈")
        upload = {'file': files}
        obj={"user":user, "fname":path}
        # request.post방식으로 파일전송.
        print("생성")
        res = requests.post(self.getIMAG_URL(user), files=upload,data = obj)
        print(res)


if __name__ =="__main__":
    T=Translator()
    print("ok")


