#-*-coding: utf-8-*-

import requests, json
from compare import UsecaseList
from RegistUser import RegistUser
#
# This module uses to Server module for managing json data.
# Specially, This module manage json data that use to send or recieve kakao server.
# ** Json data usually use HTTP Protocol's body part.
#

# 동사, 명사중 아무거나 만족 : 50
# 명사 반드시 만족 : 60
# 모두 만족: 100

mRegistUser = RegistUser()

usecase = UsecaseList()
usecase.setUsecase("water", ["마실", "음료", "물"], ["배식", "급여", "주다", "먹"], 60)
usecase.setUsecase("feed", ["밥", "먹", "사료", "간식", "식사"], ["배식", "급여", "주다", "먹"], 60)
usecase.setUsecase("open", ["문", "입구"], ["열", "오픈", "개방"], 50)
usecase.setUsecase("camera", ["사진", "상황", "모습", "얼굴", "현황"], ["보", "알", "보내"], 60)
usecase.setUsecase("regist", ["등록","사용자등록","ID등록"],["등록 ","사용자등록 ","ID등록 "], 50)

def postPiOperation(user_key,operation):
    URL, PiKey =  mRegistUser.findURLandPiKey(user_key)
    url = URL + "/" + PiKey + "/" + operation
    print(url)
    header={'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(url=url, headers = header)

    mRegistUser.closeDatabase()
    return response


class MessageClass :
    # This member function initialize kakao's keyboard setting.
    def getBaseKeyboard(self):
        baseKeyboard = {
            "type": "text"
        }
        # ** Currently, This part don't need to touch.
        return baseKeyboard

    def updatePiData(self, PiKey, userList, url):
        mRegistUser.openDatabase()
        mRegistUser.updatePiSetting(PiKey=PiKey, userList=userList, url=url)
        mRegistUser.closeDatabase()

        message = {"result": "ok"}
        return message

    # This member function send manager's message to user.
    # Also, It hava 3 ways of sending message(;feed,water,door).
    def postTextMessage(self,user_key, message):
        ##########################################################################
        # This part need to parsing message.
        # String 'message' will parse to "Noun, verbe, object".
        # And this components will make String 'result'.
        # String;result is important component to devide int 'if - else' sentence.

        result = usecase.analyzeSentence(message)

        ##########################################################################
        print(result)
        # Don't support command.

        if 'regist' in result:
            data = message.split("/")
            email = data[1].split("이메일:")[1]
            PiKey = data[2].split("고유번호:")[1]

            mRegistUser.openDatabase()
            regist_result = mRegistUser.insertUserData(user_key=user_key, email=email, PiKey=PiKey)
            mRegistUser.closeDatabase()

            if regist_result == "등록된 유저":
                sendMSG = "이미 등록된 유저입니다 :("

            elif regist_result == "등록되지 않은 키":
                sendMSG = "등록되지 않은 키입니다. 기기 고유키를 다시 확인해주세요."
            else: # regist_result == "등록 완료"
                sendMSG = "등록이 완료되었습니다!"

            postBodyMessage = {
                'message': {
                    'text': sendMSG
                },
                'keyboard': {
                    'type': 'text'
                }
            }
            return postBodyMessage

        else: #elif 'regist' in result:
            mRegistUser.openDatabase()
            isRegistedUser = mRegistUser.checkRegistedUser(user_key)
            if isRegistedUser is True:
                sendMSG = '현재 지원되지 않는 기능이예요...'
                if 'feed'in result:
                    response = postPiOperation(user_key, "feed")
                    message = response.json()
                    sendMSG = message['message']['text']


                if 'water'in result:
                    response = postPiOperation(user_key, "water")
                    message = response.json()
                    sendMSG = message['message']['text']

                if 'open'in result:
                    response = postPiOperation(user_key, "door")
                    message = response.json()
                    sendMSG = message['message']['text']


                ## This sentence is composed multimedia data;Photo.
                ## Therefore, this part only have return sentence.
                if 'camera'in result:
                    response = postPiOperation(user_key, "camera")
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

            else: # elif isRegistedUser is False
                postBodyMessage = {
                    'message': {
                        'text': "등록되지 않은 유저입니다. 사용자 등록부터 진행해주세요."
                    },
                    'keyboard': {
                        'type': 'text'
                    }
                }
                return postBodyMessage
