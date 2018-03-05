'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
import threading
import time,requests, json

class ScreenshotThread(threading.Thread):
    def __init__(self):
        self.destination = None
        self.severUtilityReference = None
        self.serverURL = "https://pethome.ga:443/"
        self.NAVER_TALK_URL = "https://gw.talk.naver.com/chatbot/v1/event"
        threading.Thread.__init__(self)
        self.screenshotEvent = threading.Event()

    def run(self):
        while not self.screenshotEvent.isSet():
            self.severUtilityReference.openDB()
            print("이미지 파일 받는중...")
            response = self.severUtilityReference.getImageFileFromPiServer(platform="naver-talk", user_key=self.destination)
            self.severUtilityReference.closeDB()
            now = time.localtime()

            PATH = "upload/"
            IMAGENAME = "Screenshot_%04d-%02d-%02d_%02d-%02d-%02d.png" % (
            now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

            with open(PATH + IMAGENAME, 'wb') as f:
                for chunk in response.iter_content(chunk_size=2048):
                    if chunk: f.write(chunk)
            f.close()

            print("image making success. %s" % (PATH + IMAGENAME))
            self.postImageToUser(PATH + IMAGENAME)
            self.screenshotEvent.clear()


    def isScreenshotThreadOnUnlock(self):
        return self.screenshotEvent.isSet()

    def setScreenshotThreadOperation(self):
        self.screenshotEvent.set()

    def setServerUtilityReference(self,ServerUtility):
        self.severUtilityReference = ServerUtility

    def setUserKey(self, user_key):
        self.destination = user_key

    def postImageToUser(self, imagepath):
        body_postImage = {
            "event": "send",
            "user": self.destination,
            "imageContent": {
                "imageUrl": self.serverURL + imagepath
            }
        }

        header = {"Content-Type": "application/json;charset=UTF-8","Authorization": "1PhwPI9cSo+vMe1BzGWK" }
        res = requests.post(url=self.NAVER_TALK_URL, headers=header, data=json.dumps(body_postImage))

