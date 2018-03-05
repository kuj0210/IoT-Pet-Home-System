from flask import Flask,jsonify
from PiInitSetting import PiSetting
from PiMessage import PiMessage
from WaterOperation import WaterOperation
#import picamera

message = PiMessage()

mPiSetting = PiSetting()
mPiSetting.ReadConfigFile()
resultByServer = mPiSetting.sendPiSettingData()

flag = {
    "isWater": False,
    "isFeed": False,
    "isDoor": False
}

feedOperationURL = "/" + mPiSetting.getPiKey() + "/feed"
waterOperationURL = "/" + mPiSetting.getPiKey() + "/water"
doorOperationURL = "/" + mPiSetting.getPiKey() + "/door"

#cameraOperationURL = "/" + mPiSetting.getPiKey() + "/camera"

app = Flask(__name__)

@app.route(feedOperationURL,methods=["POST"])
def setFeed():
    #
    # It it requeired to input Threadig function.
    # Becaues this operation must execve parrelling behaviour.
    # :: This part is "/feed". Also, it get FeedOperaion class.
    #
    return jsonify(message.getSuccessFeedMessage()), 200

@app.route(waterOperationURL, methods=["POST"])
def setWater():
    if flag["isWater"] == False:
        flag["isWater"] = True
        water = WaterOperation()
        result, flag["isWater"] = water.start()
        #with picamera.PiCamera() as camera:
        #    now = time.localtime()
        #    camera.start_preview()
        #    time.sleep(1)
        #    path = '/home/pi/Pictures/Record %04d-%02d-%02d %02d:%02d:%02d.png' % (
        #    now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        #    camera.capture(path)
        #    camera.stop_preview()

        if result is "success" :
            return jsonify(message.getSuccessWaterMessage()), 200
        elif result is "fail" :
            return jsonify(message.getFailWaterMessage()), 200

    else : # if flag["isWater"] == True:
        return jsonify(message.getContinueWaterMessage()), 200

@app.route(doorOperationURL, methods=["POST"])
def setDoor():
    #
    # It it requeired to input Threadig function.
    # Becaues this operation must execve parrelling behaviour.
    # :: This part is "/door". Also, it get doorOperaion class.
    #
    return jsonify(message.getSuccessDoorMessage()), 200


#@app.route(cameraOperationURL, methods=["POST"])
#def captureCamera():
#
#    return jsonify(message.getSuccessCameraMessage()), 200

if __name__ == "__main__":
    if resultByServer == "ok":
        app.run(host='0.0.0.0', port=8888, debug = True)
    else:
        print("RaspberryPi connection with server is denied or disconnected")