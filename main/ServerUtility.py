'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"

* ServerUtility.py
   - This module support server overall.
   - It use to send request, manage database module and is set some wrapper.
'''

import json
import requests
from RegistUser import RegistUser

class ServerUtility:
    def __init__(self):
        self.mRegistUser = RegistUser()
        self.NAVER_TALK_URL = "https://gw.talk.naver.com/chatbot/v1/event"

    
    # openDB & closeDB & getDatabase
    # : The related database module's wrapper.
    
    def openDB(self):
        self.mRegistUser.openDatabase()

    def closeDB(self):
        self.mRegistUser.closeDatabase()

    def getDatabase(self):
        return self.mRegistUser

    def postPiOperation(self, platform, user_key, operation):
        '''
        1. Arguement
            - platform : messenger application platform (Kakao-Talk & Naver-Talk-Talk)
            - user_key : Usage to find URL, PiKey (access to database).
            - operation : request to device for controlling commands.

        2. Output : response from device (Operation status : use, fail, using)

        3. Description
            This function access to database to get where device is connected, what is PiKey.
            And it send operation to device for controlling commands.
        '''
        URL, PiKey = self.mRegistUser.findURLandPiKey(platform, user_key)
        url = URL + "/" + PiKey + "/operation"
        print("Send to pi >> " + url)
        header = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url=url, headers=header, data=json.dumps(operation))

        self.mRegistUser.closeDatabase()
        return response

    def getImageFileFromPiServer(self, platform, user_key):
        '''
        1. Arguement
            - platform : messenger application platform (Kakao-Talk & Naver-Talk-Talk)
            - user_key : Usage to find URL, PiKey (access to database).
 
        2. Output : response from device (Status related recieving image)

        3. Description
            This function also access to database to get where device is connected, what is PiKey.
            And it get image-file from device for performing camera-operation.
        '''
        URL, PiKey = self.mRegistUser.findURLandPiKey(platform=platform, user_key=user_key)
        url = URL + "/" + PiKey + "/get_image"
        print("Send to pi >> " + url)
        response = requests.get(url=url, stream=True)

        return response

    def imageReciever(self, response, filename):
        '''
        1. Arguement
            - response : Who is reciever? 
            - filename : Image file to send to user.
 
        2. Output : response from device (Status related recieving image)

        3. Description
            This function also access to database to get where device is connected, what is PiKey.
            And it get image-file from device for performing camera-operation.
        '''
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=2048):
                if chunk: f.write(chunk)
        f.close()

    def updatePiData(self, PiKey, kakaoUserList, naverUserList, url):
        '''
        1. Arguement
            - PiKey : Device information that is registed in database.
            - kakaoUserList & naverUserList : The userlist that is registed in database.
            - url : URL the device is connected.
 
        2. Output : Permission to connect to server. 
                   (Server check that this device is registed. If not, the device don't connect this server.)
 
        3. Description
            If the device is turned on and try to connect this server, this function is executed.
            If this device is the registed device to server, server will update database data related the device.
            And then server will send data that database-renew is completed and permit to device to connect this server.
        '''
        self.mRegistUser.openDatabase()
        self.mRegistUser.updatePiSetting(PiKey=PiKey, kakaoUserList=kakaoUserList, naverUserList=naverUserList, url=url)
        self.mRegistUser.closeDatabase()

        message = {"result": "ok"}
        return message

    def postToNaverTalk(self, body):
        '''
        1. Arguement
            - body : The part of sending body to user.

        2. Description
            The main server send the request to naver-talk-talk API server.
        '''
        header = {"Content-Type": "application/json;charset=UTF-8","Authorization": "1PhwPI9cSo+vMe1BzGWK" }
        res = requests.post(url=self.NAVER_TALK_URL, headers=header, data=json.dumps(body))
