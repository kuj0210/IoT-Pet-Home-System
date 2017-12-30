#-*-coding: utf-8-*-

import requests, json
from compare import UsecaseList
#
# This module uses to Server module for managing json data.
# Specially, This module manage json data that use to send or recieve kakao server.
# ** Json data usually use HTTP Protocol's body part.
#

# 동사, 명사중 아무거나 만족 : 50
# 명사 반드시 만족 : 60
# 모두 만족: 100

usecase = UsecaseList()
usecase.setUsecae("water", ["마실", "음료", "물"], ["배식", "급여", "주다", "먹"], 60)
usecase.setUsecae("feed", ["밥", "먹", "사료", "간식", "식사"], ["배식", "급여", "주다", "먹"], 60)
usecase.setUsecae("open", ["문", "입구"], ["열", "오픈", "개방"], 50)
usecase.setUsecae("camera", ["사진", "상황", "모습", "얼굴", "현황"], ["보", "알", "보내"], 60)

def postPiOperation(operation):
    param = {'type':'test'}
    url = 'http://localhost:8888/' + operation
    header={'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(url=url, headers = header, data=json.dumps(param))
    return response


class MessageClass :
    # This member function initialize kakao's keyboard setting.
    def getBaseKeyboard(self):
        baseKeyboard = {
            "type": "text"
        }
        # ** Currently, This part don't need to touch.
        return baseKeyboard

    # This member function send manager's message to user.
    # Also, It hava 3 ways of sending message(;feed,water,door).
    def postTextMessage(self, message):
        ##########################################################################
        # This part need to parsing message.
        # String 'message' will parse to "Noun, verbe, object".
        # And this components will make String 'result'.
        # String;result is important component to devide int 'if - else' sentence.

        result = usecase.analyzeSentence(message)

        ##########################################################################
        print(result)
        # Don't support command.

        sendMSG = '현재 지원되지 않는 기능이예요...'
        if 'feed'in result:
            response = postPiOperation("feed")
            message = response.json()
            sendMSG = message['message']['text']


        if 'water'in result:
            response = postPiOperation("water")
            message = response.json()
            sendMSG = message['message']['text']

        if 'open'in result:
            response = postPiOperation("door")
            message = response.json()
            sendMSG = message['message']['text']


        ## This sentence is composed multimedia data;Photo.
        ## Therefore, this part only have return sentence.
        if 'camera'in result:
            response = postPiOperation("camera")
            message = response.json()
            sendMSG = message['message']['text']
            postBodyMessage = {
                'message': {
                    'text': sendMSG,
                    'photo': {
                        "url": "://mud-kage.kakao.co.kr/dn/NTmhS/btqfEUdFAUf/FjKzkZsnoeE4o19klTOVI1/openlink_640x640s.jpg",
                        'width': 640,
                        'height': 640
                    }
                },
                'keyboard': {
                    'type': 'text'
                }
            }
            return postBodyMessage


        else :
            # Parsing and reunit message return to Server module.
            postBodyMessage = {
                    'message': {
                        'text': sendMSG
                    },
                    'keyboard': {
                        'type': 'text'
                    }
                }
            return postBodyMessage
