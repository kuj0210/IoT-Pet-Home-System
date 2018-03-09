'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
#-*-coding: utf-8-*-

from ServerManagerForKakao import KakaoMessageClass
from ServerManagerForNaver import NaverMessageClass
from flask import Flask,request,jsonify,send_from_directory
from compare import UsecaseList
from ServerUtility import ServerUtility

naverMessage = NaverMessageClass()
kakaoMessage = KakaoMessageClass()
mServerUtility = ServerUtility()

usecase = UsecaseList()
usecase.setUsecase("water", ["마실", "음료", "물"], ["배식", "급여", "주다", "먹"], 60)
usecase.setUsecase("feed", ["밥", "먹", "사료", "간식", "식사","식"], ["배식", "급여", "주다", "먹"], 60)
usecase.setUsecase("door", ["문", "입구"], ["열", "오픈", "개방"], 50)
usecase.setUsecase("camera", ["사진", "상황", "모습", "얼굴", "현황"], ["보", "알", "보내"], 60)
usecase.setUsecase("regist", ["[등록]"],["[등록]"], 50)
usecase.setUsecase("information",["[정보]"],["[정보]"],50)
usecase.setUsecase("howToUse",["[사용법]","[도우미]","[도움말]"],["[사용법]","[도우미]","[도움말]"],50)

UPLOAD_FOLDER = 'uploaded'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/",methods=["POST"])
def naver_ServerManager():
    data = request.get_json()
    return jsonify(naverMessage.manageEvent(data=data, usecase=usecase)),200

@app.route("/keyboard",methods =["GET"])
def kakao_Keyboard():
    return jsonify(kakaoMessage.getBaseKeyboard()),200

@app.route("/message",methods=["POST"])
def kakao_Message():
    data = request.get_json()
    user_key = data['user_key']
    message = data['content']
    return jsonify(kakaoMessage.manageRequest(user_key=user_key, message=message, usecase=usecase)), 200

@app.route("/friend",methods=["POST"])
def kakao_AddFriend():
    return "HTTP/1.1 200 OK"

@app.route("/friend/<user_key>", methods=["DELETE"])
def kakao_DeleteFriend(user_key):
    return "HTTP/1.1 200 OK"

@app.route("/chat_room/<user_key>",methods=["DELETE"])
def kakao_chat_roomOut():
    return "HTTP/1.1 200 OK"

@app.route("/pi_regist", methods=["POST"])
def settingPi():
    data = request.get_json()
    PiKey = data["PiKey"]
    kakaoUserList = data["userList"]["kakao"]
    naverUserList = data["userList"]["naver"]
    url = data["url"]

    return jsonify(mServerUtility.updatePiData(PiKey, kakaoUserList, naverUserList, url)), 200

@app.route('/download/<filename>', methods=['GET'])
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename)

@app.route('/push', methods=["POST"])
def push_alarm():
    data = request.get_json()
    PiKey = data["PiKey"]
    message = data["message"]
    naverMessage.sendEventForPush(PiKey, message)
    return "HTTPS/1.1 200 OK"

if __name__ == "__main__":
    ssl_cert = '/etc/letsencrypt/live/pethome.ga/fullchain.pem'
    ssl_key =  '/etc/letsencrypt/live/pethome.ga/privkey.pem'
    contextSSL =  (ssl_cert, ssl_key)
    app.run(host='0.0.0.0', port=443, debug = True, ssl_context = contextSSL)

