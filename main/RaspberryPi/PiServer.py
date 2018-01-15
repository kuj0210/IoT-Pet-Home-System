from flask import Flask,jsonify,request, send_from_directory
from PiInitSetting import PiSetting
from PiMessage import PiMessage
from FeedOperation import FeedOperation
from WaterOperation import WaterOperation
from DoorOperation import DoorOperation
from CameraOperation import CameraOperation

message = PiMessage()

mPiSetting = PiSetting()
mPiSetting.ReadConfigFile()
resultByServer = mPiSetting.sendPiSettingData()
cameraOperation = CameraOperation()

feedOperation = FeedOperation()
waterOperation = WaterOperation()
doorOperation = DoorOperation()

flag = {
    "isWater": False,
    "isFeed": False,
    "isDoor": False,
    "isCamera" : False
}
operationURL = "/" + mPiSetting.getPiKey() + "/operation"
operationCameraUploadURL = "/" + mPiSetting.getPiKey() + "/get_image"
NOT_SUPPORT = "현재 지원하지 않는 기능입니다 :("

app = Flask(__name__, static_folder='image')

@app.route(operationURL, methods=["POST"])
def getOperationByServer():
    data = request.get_json()
    operation = data["operation"]
    sendMSG = NOT_SUPPORT
    if "feed" in operation:
        if flag["isFeed"] is False:
            flag["isFeed"] = True
            result, flag["isFeed"] = feedOperation.run()
            flag["isFeed"] = False

            if result == "success":
                if sendMSG == NOT_SUPPORT:
                    sendMSG = message.getSuccessFeedMessage()
                else: #sendMSG is not None:
                    sendMSG += "\n" + message.getSuccessFeedMessage()
            else: #flag["isFeed"] is "fail":
                if sendMSG == NOT_SUPPORT:
                    sendMSG += message.getFailFeedMessage()
                else: #sendMSG is not None:
                    sendMSG += "\n" + message.getFailFeedMessage()
        else:  # flag["isFeed"] is True
            if sendMSG == NOT_SUPPORT:
                sendMSG += message.getContinueFeedMessage()
            else:  # sendMSG is not None:
                sendMSG += "\n" + message.getContinueFeedMessage()


    if "water" in operation:
        if flag["isWater"] is False:
            flag["isWater"] = True
            result, flag["isWater"] = waterOperation.run()
            flag["isWater"] = False

            if result == "success":
                if sendMSG == NOT_SUPPORT:
                    sendMSG = message.getSuccessWaterMessage()
                else: #sendMSG is not None:
                    sendMSG += "\n" + message.getSuccessWaterMessage()
            else: #flag["isWater"] is "fail":
                if sendMSG == NOT_SUPPORT:
                    sendMSG = message.getFailWaterMessage()
                else: #sendMSG is not None:
                    sendMSG += "\n" + message.getFailWaterMessage()
        else:  # flag["isWater"] is True
            if sendMSG == NOT_SUPPORT:
                sendMSG = message.getContinueWaterMessage()
            else:  # sendMSG is not None:
                sendMSG += "\n" + message.getContinueWaterMessage()

    if "open" in operation:
        if flag["isDoor"] is False:
            flag["isDoor"] = True
            doorOperation.run()
            flag["isDoor"] = False

            if sendMSG == NOT_SUPPORT:
                sendMSG = message.getContinueDoorMessage()
            else:  # sendMSG is not None:
                sendMSG += "\n" + message.getContinueDoorMessage()

        else:  # flag["isDoor"] is True
            if sendMSG == NOT_SUPPORT:
                sendMSG = message.getFailDoorMessage()
            else:  # sendMSG is not None:
                sendMSG += "\n" + message.getFailMessage()

    if "camera" in operation:
        if flag["isCamera"] is False:
            flag["isCamera"] = True
            result, flag["isCamera"] = cameraOperation.run()
            flag["isCamera"] = False
            imagePath = "upload/" + cameraOperation.getFilename()

            if result == "success":
                if sendMSG == NOT_SUPPORT:
                    sendMSG = message.getSuccessCameraMessage()
                else:  # sendMSG is not None:
                    sendMSG += "\n" + message.getSuccessCameraMessage()
            else:  # flag["isDoor"] is "fail":
                if sendMSG == NOT_SUPPORT:
                    sendMSG = message.getFailCameraMessage()
                else:  # sendMSG is not None:
                    sendMSG += "\n" + message.getFailCameraMessage()
        else:  # flag["isDoor"] is True
            if sendMSG == NOT_SUPPORT:
                sendMSG = message.getContinueCameraMessage()
            else:  # sendMSG is not None:
                sendMSG += "\n" + message.getContinueCameraMessage()

        postToServerMessage = {"message": {"text": sendMSG, "camera": True}}
        return jsonify(postToServerMessage)

    else:
        postToServerMessage = {"message": {"text": sendMSG ,"camera":False} }
        return jsonify(postToServerMessage)

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

        app.run(host='0.0.0.0', port=8888, debug = True)
    else:
        print("RaspberryPi connection with server is denied or disconnected")
