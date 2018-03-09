'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
from flask import Flask,jsonify,request, send_from_directory
from PiServerUtility import PiSetting

mPiSetting = PiSetting()
mPiSetting.ReadConfigFile()
PiKey = mPiSetting.getPiKey()

operationURL = "/" + mPiSetting.getPiKey() + "/operation"
operationCameraUploadURL = "/" + mPiSetting.getPiKey() + "/get_image"

app = Flask(__name__, static_folder='image')

@app.route(operationURL, methods=["POST"])
def getOperationByServer():
    data = request.get_json()
    operation = data["operation"]
    postStatusToServer = mPiSetting.makePiData(operation=operation)

    return jsonify(postStatusToServer)

@app.route(operationCameraUploadURL, methods=['GET'])
def send_file():
    filename = mPiSetting.getFilename()
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    resultByServer = mPiSetting.sendPiSettingData()

    if resultByServer == "ok":
        mPiSetting.device_and_thread__init__(PiKey=PiKey)

        try:
            app.run(host='0.0.0.0', port=8888)

        except KeyboardInterrupt:
            print("PiServer is disconnected")
            #GPIO.cleanup()
    else:
        print("RaspberryPi connection with server is denied or disconnected")
