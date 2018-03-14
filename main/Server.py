'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"

* Server.py
  - Core Modules That Work with Server.
  - Perform the role of the main server by running this module
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

'''
 Content with the verb or noun : 50
 It must content with noun : 60
 All content with verb and noun: 100
'''
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
'''
- Related Naver-talk-talk Platform
- This function manage the related Naver-talk-talk API 
  and reply to Naver-talk-talk API server.  
'''
    data = request.get_json()
    return jsonify(naverMessage.manageEvent(data=data, usecase=usecase)),200

@app.route("/keyboard",methods =["GET"])
def kakao_Keyboard():
'''
- Related Kakao-talk Platform
- This function initialize and call kakao_talk's keyboard.
'''
    return jsonify(kakaoMessage.getBaseKeyboard()),200

@app.route("/message",methods=["POST"])
def kakao_Message():
'''
- Related Kakao-talk Platform
- This function manage message(text) from Kakao-platform client
  and reply a appropriate message to the client.
'''
    data = request.get_json()
    user_key = data['user_key']
    message = data['content']
    return jsonify(kakaoMessage.manageRequest(user_key=user_key, message=message, usecase=usecase)), 200

@app.route("/friend",methods=["POST"])
def kakao_AddFriend():
'''
- Related Kakao-talk Platform
- This function manage request about adding friend.
- Send only 200 OK responses, as there is nothing special to manage with the request.
'''
    return "HTTP/1.1 200 OK"

@app.route("/friend/<user_key>", methods=["DELETE"])
def kakao_DeleteFriend(user_key):
'''
- Related Kakao-talk Platform
- This function manage request about deleting friend.
- Send only 200 OK responses, as there is nothing special to manage with the request.
'''
    return "HTTP/1.1 200 OK"

@app.route("/chat_room/<user_key>",methods=["DELETE"])
def kakao_chat_roomOut():
'''
- Related Kakao-talk Platform
- This function manage request about joining chatting room.
- Send only 200 OK responses, as there is nothing special to manage with the request.
'''
    return "HTTP/1.1 200 OK"

@app.route("/pi_regist", methods=["POST"])
def settingPi():
'''
- Related to control Raspberry-Pi
- This function initialize the related device.
- When the device is turned on, it is a function of receiving and processing a request.
'''
    data = request.get_json()
    PiKey = data["PiKey"]
    kakaoUserList = data["userList"]["kakao"]
    naverUserList = data["userList"]["naver"]
    url = data["url"]

    return jsonify(mServerUtility.updatePiData(PiKey, kakaoUserList, naverUserList, url)), 200

@app.route('/download/<filename>', methods=['GET'])
def send_file(filename):
'''
- Only related Kakao-talk Platform
- This function send the image file:<filename> to client who request this image file.
'''
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename)

@app.route('/push', methods=["POST"])
def push_alarm():
'''
- Only related Naver-talk-talk Platform
- This function is intended to provide alarm services to the user.
'''
    data = request.get_json()
    PiKey = data["PiKey"]
    message = data["message"]
    naverMessage.sendEventForPush(PiKey, message)
    return "HTTPS/1.1 200 OK"

if __name__ == "__main__":
'''
It's the main part. After you set up the SSL certificate path, 
attach it to the flask framework and launch the Web server.
'''
    ssl_cert = '/etc/letsencrypt/live/pethome.ga/fullchain.pem'
    ssl_key =  '/etc/letsencrypt/live/pethome.ga/privkey.pem'
    contextSSL =  (ssl_cert, ssl_key)
    app.run(host='0.0.0.0', port=443, debug = True, ssl_context = contextSSL)

