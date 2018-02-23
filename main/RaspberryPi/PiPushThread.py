import threading
import time
import requests, json
import os

class PiPushThread(threading.Thread):
    def __init__(self, PiKey):
        self.waterCounter = 0 # 1 minute == 1 count
        self.feedCounter = 0
        self.PiKey = PiKey
        self.SERVER_URL = "https://pethome.ga:443/push"
        self.HEADER = {'Content-Type': 'application/json; charset=utf-8'}
        threading.Thread.__init__(self)
        self.sem = threading.Semaphore(1)

    def run(self):
        self.sendWaterPush()
        while True:
            time.sleep(1)

            if os.path.exists("fifo"):
                fifo = open("fifo", "r")
                result = fifo.read()
                if len(result) == 0:
                    self.waterCounter += 1
                    self.feedCounter += 1

                elif result == "FEED_DONE":
                    self.feedCounter = 0
                elif result == "WATER_DONE":
                    self.waterCounter = 0

            if self.waterCounter == 10:
                self.sendWaterPush()

            if self.feedCounter == 10:
                self.sendFeedPush()

    def sendFeedPush(self):
        counter = self.feedCounter / 10

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
        counter = self.waterCounter / 10

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

        requests.post(url=self.SERVER_URL, headers=self.HEADER, data=json.dumps(postToServer))

