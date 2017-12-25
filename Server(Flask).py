import socket, threading
import json

from flask import Flask,request,jsonify

baseKeyboard = {
    "type":"text"
}

feedMessage = {
    'message':{
        'text':'우리 애완용에게 밥을 주고 있어요.'
    },
    'keyboard':{
        'type':'text'
    }
}

waterMessage = {
    'message':{
        'text':'우리 애완용에게 물을 주고 있어요.'
    },
    'keyboard':{
        'type':'text'
    }
}

doorMessage = {
    'message':{
        'text':'애완용 집 문을 열어줍니다 :)'
    },
    'keyboard':{
        'type':'text'
    }
}

cameraMessage = {
    'message':{
        'text':'사진을 찍었어요!',
        'photo':'/photo/pet.png',
        'width':640,
        'height':480
    },
    'keyboard':{
        'type':'text'
    }
}

errorMessage = {
    'message':{
        'text':'현재 지원되지 않는 기능이예요.'
    },
    'keyboard':{
        'type':'text'
    }
}

## json 타입들 초기화

app = Flask(__name__)

## Flask 키는 소스

@app.route("/keyboard",methods =["GET"])
def keyboard():
    return jsonify(baseKeyboard),200

## 키보드 정보 가져옴

@app.route("/message",methods=["POST"])
def message():
    data = request.get_json()   ## 요청메세지로부터 json 데이터를 가져옴
                                ## 게다가 딕셔너리 형태로 반환해줌
    print("User -> Server : ")
    print(data)
    message = data['content']

    if message == "feed":
        print("Server -> user : ")
        print(json.dumps(feedMessage))
        return jsonify(feedMessage), 200
    elif message == "water":
        print("Server -> user : ")
        print(json.dumps(waterMessage))
        return jsonify(waterMessage), 200
    elif message == "door":
        print("Server -> user : ")
        print(json.dumps(doorMessage))
        return jsonify(doorMessage), 200
    elif message == "camera":
        print("Server -> user : ")
        print(json.dumps(cameraMessage))
        return jsonify(cameraMessage), 200
    else:
        print("Server -> user : ")
        print(json.dumps(errorMessage))
        return jsonify(errorMessage), 200

## 메세지를 보냈을 때 처리

@app.route("/friend",methods=["POST"])
def friendAdd():
    message = request.get_json()
    user_key = message['user_key']
    print("Friend: Add friend : " + user_key)
    return "HTTP/1.1 200 OK"
## 친구 추가했을 때

@app.route("/friend/<user_key>", methods=["DELETE"])
def friendDelete(user_key):
    print("Friend: Delete friend = " + user_key)
    return "HTTP/1.1 200 OK"
## 친구 삭제했을 때

@app.route("/chat_room/<user_key>",methods=["DELETE"])
def chat_roomOut(user_key):
    print("chat_room: User go out = " + user_key)
    return "HTTP/1.1 200 OK"
## 채팅방에서 나갔을 때

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug = True)