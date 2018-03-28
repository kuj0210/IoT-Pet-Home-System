'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
import threading
import time
import requests, json
import os

class PiPushThread(threading.Thread):
    '''
    This class is related push-alarm service for sending main-server.
    And this class is thread and executed in back-ground.
    '''
    def __init__(self):
        self.waterCounter = 0 # 1 minute == 1 count
        self.feedCounter = 0
        self.PiKey = "None"
        self.SERVER_URL = "https://pethome.ga:443/push"
        self.HEADER = {'Content-Type': 'application/json; charset=utf-8'}
        threading.Thread.__init__(self)

    def run(self):
        '''
        Description
            This function send push-alarm data to main-server. And this is core part in this func.
            In addition, default alarm setting is 1 hour ( water and feed ).
        '''
        while True:
            time.sleep(60)
            result = os.getenv("PUSH")

            if result == "NONE":
                self.waterCounter += 1
                self.feedCounter += 1
            elif result == "FEED":
                self.feedCounter = 0
            elif result == "WATER":
                self.waterCounter = 0

            if self.waterCounter == 60:
                self.sendWaterPush()

            if self.feedCounter == 60:
                self.sendFeedPush()

            os.environ["PUSH"] = "NONE"

    def getPiKey(self, PiKey):
        self.PiKey = PiKey

    '''
    Description
        Below 2 functions send json type data to main-server. This data will be push-service.
        But this function only support in naver-talk-talk platform, now.
    '''
    def sendFeedPush(self):
        counter = self.feedCounter / 60

        postToServer = {
            "PiKey": self.PiKey,
            "message": {
                "fromPi": True,
                "sensor": {
                    "list": "feed",
                    "feed": {
                        "time": counter
                    }
                },
            }
        }

        try:
            requests.post(url=self.SERVER_URL, headers=self.HEADER, data=json.dumps(postToServer))
        except:
            print("main server error...")

    def sendWaterPush(self):
        counter = self.waterCounter / 60

        postToServer = {
            "PiKey" : self.PiKey,
            "message" : {
                "fromPi" : True,
                "sensor" : {
                    "list" : "water",
                    "water" : {
                        "time" : counter
                    }
                },
            }
        }

        try:
            requests.post(url=self.SERVER_URL, headers=self.HEADER, data=json.dumps(postToServer))
        except:
            print("main server error...")
