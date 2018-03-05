from flask import Flask,request,jsonify
from JsonMessage import MessageClass

## json 타입들 초기화

mMessage = MessageClass()
app = Flask(__name__)
## Flask 키는 소스

@app.route("/keyboard",methods =["GET"])
def keyboard():
    return jsonify(mMessage.getBaseKeyboard()),200

## 키보드 정보 가져옴

@app.route("/message",methods=["POST"])
def message():
    data = request.get_json()   ## 요청메세지로부터 json 데이터를 가져옴
                                ## 게다가 딕셔너리 형태로 반환해줌
    #print("User -> Server : ")
    #print(data)
    message = data['content']
    return jsonify(mMessage.postTextMessage(message=message)),200
## 메세지를 보냈을 때 처리

@app.route("/friend",methods=["POST"])
def friendAdd():
    message = request.get_json()
    user_key = message['user_key']
    #print("Friend: Add friend : " + user_key)
    return "HTTP/1.1 200 OK"
## 친구 추가했을 때

@app.route("/friend/<user_key>", methods=["DELETE"])
def friendDelete(user_key):
    #print("Friend: Delete friend = " + user_key)
    return "HTTP/1.1 200 OK"
## 친구 삭제했을 때

@app.route("/chat_room/<user_key>",methods=["DELETE"])
def chat_roomOut(user_key):
    #print("chat_room: User go out = " + user_key)
    return "HTTP/1.1 200 OK"
## 채팅방에서 나갔을 때

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug = True)
