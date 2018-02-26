from flask import Flask,jsonify,request, send_from_directory
from PiInitSetting import PiSetting
from FeedOperation import FeedOperation
from WaterOperation import WaterOperation
from DoorOperation import DoorOperation
from CameraOperation import CameraOperation
from PiPushThread import PiPushThread
import os

mPiSetting = PiSetting()
mPiSetting.ReadConfigFile()
resultByServer = mPiSetting.sendPiSettingData()
PiKey = mPiSetting.getPiKey()

cameraOperation = CameraOperation()
feedOperation = FeedOperation()
waterOperation = WaterOperation()
doorOperation = DoorOperation()
pushThread = PiPushThread()
os.environ["PUSH"] = "NONE"

operationURL = "/" + mPiSetting.getPiKey() + "/operation"
operationCameraUploadURL = "/" + mPiSetting.getPiKey() + "/get_image"

app = Flask(__name__, static_folder='image')

@app.route(operationURL, methods=["POST"])
def getOperationByServer():
    data = request.get_json()
    operation = data["operation"]
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

    return jsonify(postStatusToServer)

@app.route(operationCameraUploadURL, methods=['GET'])
def send_file():
    filename = cameraOperation.getFilename()
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    if resultByServer == "ok":
        water_pin = 12
        feed_pin = 19
        door_pin = 18

       GPIO.setmode(GPIO.BCM)

        try:
            GPIO.setup(water_pin, GPIO.OUT)
            wp = GPIO.PWM(water_pin, 50)
            print("Water Operation Setting complete.")
        except:
            print("Error : In Water Operation")

        try:
            GPIO.setup(feed_pin, GPIO.OUT)
            fp = GPIO.PWM(feed_pin, 50)
            print("Feed Operation Setting complete.")
        except:
            print("Error : In Feed Operation")

        try:
            GPIO.setup(door_pin, GPIO.OUT)
            dp = GPIO.PWM(door_pin, 50)
            print("Door Operation Setting complete.")
        except:
            print("Error : In Door Operation")

        waterOperation.setPin(wp)
        feedOperation.setPin(fp)
        doorOperation.setPin(dp)

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

        app.run(host='0.0.0.0', port=8888)
    else:
        print("RaspberryPi connection with server is denied or disconnected")
