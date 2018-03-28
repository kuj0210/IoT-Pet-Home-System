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
    '''
    Description
        If you recieve a operation list from main-server, this function request the operations to appropriate modules.
        And this func get the result data from each modules and send it to main-server.
    '''
    data = request.get_json()
    operation = data["operation"]
    postStatusToServer = mPiSetting.makePiData(operation=operation)

    return jsonify(postStatusToServer)

@app.route(operationCameraUploadURL, methods=['GET'])
def send_file():
    '''
    Description
        If main-server request to get imagefile, this function send a imagefile to main-server.
    '''
    filename = mPiSetting.getFilename()
    return send_from_directory(app.static_folder, filename)

if __name__ == "__main__":
    '''
    Description
        1. You turn on this device, it execute this part.
        2. Send the registed device information to main-server.
        3. Recieve the response to main-server and if response is "ok", you can use this device.
    '''
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
