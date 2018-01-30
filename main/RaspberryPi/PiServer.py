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
        if not feedOperation.isFeedOnUnlock():
            feedOperation.setFeedOperation()
            if sendMSG == NOT_SUPPORT :
                sendMSG = message.getContinueFeedMessage()
            else :
                sendMSG += "\n" + message.getContinueFeedMessage()

        else:
            if sendMSG == NOT_SUPPORT :
                sendMSG = message.getFailFeedMessage()
            else :
                sendMSG += "\n" + message.getFailFeedMessage()

    if "water" in operation:
        if not waterOperation.isWaterOnUnlock():
            waterOperation.setWaterOperation()
            if sendMSG == NOT_SUPPORT :
                sendMSG = message.getContinueWaterMessage()
            else :
                sendMSG += "\n" + message.getContinueWaterMessage()

        else:
            if sendMSG == NOT_SUPPORT :
                sendMSG = message.getFailWaterMessage()
            else :
                sendMSG += "\n" + message.getFailWaterMessage()

    if "open" in operation:
        if not doorOperation.isDoorOnUnlock():
            doorOperation.setDoorOperation()
            if sendMSG == NOT_SUPPORT :
                sendMSG = message.getContinueDoorMessage()
            else :
                sendMSG += "\n" + message.getContinueDoorMessage()

        else:
            if sendMSG == NOT_SUPPORT :
                sendMSG = message.getFailDoorMessage()
            else :
                sendMSG += "\n" + message.getFailDoorMessage()

    if "camera" in operation:
        imagePath = "upload/" + cameraOperation.getFilename()
        postToServerMessage = {"message": {"text": None, "camera": True}}

        if not doorOperation.isDoorOnUnlock():
            cameraOperation.setCameraOperation()
            result = cameraOperation.run()
            cameraOperation.join()

            if result == "success":
                if sendMSG == NOT_SUPPORT:
                    sendMSG = message.getSuccessCameraMessage()
                else:  # sendMSG is not None:
                    sendMSG += "\n" + message.getSuccessCameraMessage()

                postToServerMessage["message"]["text"] = sendMSG

            else:  # flag["isDoor"] is "fail":
                if sendMSG == NOT_SUPPORT:
                    sendMSG = message.getFailCameraMessage()
                else:  # sendMSG is not None:
                    sendMSG += "\n" + message.getFailCameraMessage()

                postToServerMessage["message"]["text"] = sendMSG
                postToServerMessage["message"]["camera"] = False

        else:  # flag["isDoor"] is "fail":
            if sendMSG == NOT_SUPPORT:
                sendMSG = message.getFailCameraMessage()
            else:  # sendMSG is not None:
                sendMSG += "\n" + message.getFailCameraMessage()

            postToServerMessage["message"]["text"] = sendMSG
            postToServerMessage["message"]["camera"] = False

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

       #GPIO.setmode(GPIO.BCM)

        try:
        #    GPIO.setup(water_pin, GPIO.OUT)
        #   wp = GPIO.PWM(water_pin, 50)
            print("Water Operation Setting complete.")
        except:
            print("Error : In Water Operation")

        try:
        #    GPIO.setup(feed_pin, GPIO.OUT)
        #    fp = GPIO.PWM(feed_pin, 50)
            print("Feed Operation Setting complete.")
        except:
            print("Error : In Feed Operation")

        try:
        #    GPIO.setup(door_pin, GPIO.OUT)
        #    dp = GPIO.PWM(door_pin, 50)
            print("Door Operation Setting complete.")
        except:
            print("Error : In Door Operation")

        #waterOperation.setPin(wp)
        #feedOperation.setPin(fp)
        #doorOperation.setPin(dp)

        waterOperation.start()
        feedOperation.start()
        doorOperation.start()

        app.run(host='0.0.0.0', port=8888, debug = True)
    else:
        print("RaspberryPi connection with server is denied or disconnected")
