'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
import json
import requests
from RegistUser import RegistUser

class ServerUtility:
    def __init__(self):
        self.mRegistUser = RegistUser()
        self.NAVER_TALK_URL = "https://gw.talk.naver.com/chatbot/v1/event"

    def openDB(self):
        self.mRegistUser.openDatabase()

    def closeDB(self):
        self.mRegistUser.closeDatabase()

    def getDatabase(self):
        return self.mRegistUser

    def postPiOperation(self, platform, user_key, operation):
        URL, PiKey = self.mRegistUser.findURLandPiKey(platform, user_key)
        url = URL + "/" + PiKey + "/operation"
        print("Send to pi >> " + url)
        header = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url=url, headers=header, data=json.dumps(operation))

        self.mRegistUser.closeDatabase()
        return response

    def getImageFileFromPiServer(self, platform, user_key):
        URL, PiKey = self.mRegistUser.findURLandPiKey(platform=platform, user_key=user_key)
        url = URL + "/" + PiKey + "/get_image"
        print("Send to pi >> " + url)
        response = requests.get(url=url, stream=True)

        return response

    def imageReciever(self, response, filename):
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=2048):
                if chunk: f.write(chunk)
        f.close()

    def updatePiData(self, PiKey, kakaoUserList, naverUserList, url):
        self.mRegistUser.openDatabase()
        self.mRegistUser.updatePiSetting(PiKey=PiKey, kakaoUserList=kakaoUserList, naverUserList=naverUserList, url=url)
        self.mRegistUser.closeDatabase()

        message = {"result": "ok"}
        return message

    def postToNaverTalk(self, body):
        header = {"Content-Type": "application/json;charset=UTF-8","Authorization": "1PhwPI9cSo+vMe1BzGWK" }
        res = requests.post(url=self.NAVER_TALK_URL, headers=header, data=json.dumps(body))