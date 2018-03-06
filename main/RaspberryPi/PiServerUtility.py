'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
import requests, json, socket, os

from CameraOperation import CameraOperation
from DoorOperation import DoorOperation
from FeedOperation import FeedOperation
from PiPushThread import PiPushThread
from WaterOperation import WaterOperation

cameraOperation = CameraOperation()
feedOperation = FeedOperation()
waterOperation = WaterOperation()
doorOperation = DoorOperation()
pushThread = PiPushThread()

os.environ["PUSH"] = "NONE"

class PiSetting:
    def __init__(self):
        self.configFile = "config-pi.txt"
        self.PiKey = ""
        self.kakaoUserList = []
        self.naverUserList = []

    def ReadConfigFile(self):
        fp = open(self.configFile,"r")

        # First line is PiKey.
        self.PiKey = fp.readline().split("\n")[0]

        # Another lines is user list(email).

        line = fp.readline()
        result = line.split("\n")[0]
        if "__kakao__" in result:
            while True:
                line = fp.readline()
                if not line: break
                email = line.split("\n")[0]
                if "__naver__" in email: break
                self.kakaoUserList.append(email)

            while True:
                line = fp.readline()
                if not line: break
                email = line.split("\n")[0]
                self.naverUserList.append(email)

        fp.close()
        print(self.kakaoUserList)
        print(self.naverUserList)

    def sendPiSettingData(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 1))
        ipAddress = s.getsockname()[0]
        url = "http://" + ipAddress + ":8888"
        postMessage = {
            "PiKey" : self.PiKey,
            "userList": {
                "kakao" : self.kakaoUserList,
                "naver" : self.naverUserList
            },
            "url": url
        }
        SERVER_URL = "https://pethome.ga:443/pi_regist"
        HEADER = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url=SERVER_URL, headers=HEADER, data=json.dumps(postMessage))

        message = response.json()
        result = message["result"]
        return result

    def device_and_thread__init__(self, PiKey):
        #water_pin = 12
        #feed_pin = 19
        #door_pin = 18

        #GPIO.setmode(GPIO.BCM)

        try:
            #GPIO.setup(water_pin, GPIO.OUT)
            #wp = GPIO.PWM(water_pin, 50)
            print("Water Operation Setting complete.")
        except:
            print("Error : In Water Operation")

        try:
            #GPIO.setup(feed_pin, GPIO.OUT)
            #fp = GPIO.PWM(feed_pin, 50)
            print("Feed Operation Setting complete.")
        except:
            print("Error : In Feed Operation")

        try:
            #GPIO.setup(door_pin, GPIO.OUT)
            #dp = GPIO.PWM(door_pin, 50)
            print("Door Operation Setting complete.")
        except:
            print("Error : In Door Operation")

        #waterOperation.setPin(wp)
        #feedOperation.setPin(fp)
        #doorOperation.setPin(dp)

        waterOperation.daemon = True
        feedOperation.daemon = True
        doorOperation.daemon = True
        cameraOperation.daemon = True

        waterOperation.start()
        feedOperation.start()
        doorOperation.start()
        cameraOperation.start()

        pushThread.getPiKey(PiKey=PiKey)
        pushThread.start()

    def makePiData(self, operation):
        postStatusToServer = {
            "camera": "unuse",
            "feed": "unuse",
            "water": "unuse",
            "door": "unuse"
        }

        if "feed" in operation:
            if not feedOperation.isFeedOnUnlock():
                feedOperation.setFeedOperation()
                postStatusToServer["feed"] = "use"

            else:
                postStatusToServer["feed"] = "using"

        if "water" in operation:
            if not waterOperation.isWaterOnUnlock():
                waterOperation.setWaterOperation()
                postStatusToServer["water"] = "use"

            else:
                postStatusToServer["water"] = "using"

        if "door" in operation:
            if not doorOperation.isDoorOnUnlock():
                doorOperation.setDoorOperation()
                postStatusToServer["door"] = "use"

            else:
                postStatusToServer["door"] = "using"

        if "camera" in operation:
            if not cameraOperation.isCameraOnUnlock():
                cameraOperation.setCameraOperation()
                postStatusToServer["camera"] = "use"

            else:  # flag["isCamera"] is "fail":
                postStatusToServer["camera"] = "using"

        return postStatusToServer

    def getPiKey(self):
        return self.PiKey

    def getFilename(self):
        return cameraOperation.getFilename()