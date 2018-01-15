#-*-coding: utf-8-*-

import requests, json
from compare import UsecaseList
from RegistUser import RegistUser
import time
#
# This module uses to Server module for managing json data.
# Specially, This module manage json data that use to send or recieve kakao server.
# ** Json data usually use HTTP Protocol's body part.
#

# 동사, 명사중 아무거나 만족 : 50
# 명사 반드시 만족 : 60
# 모두 만족: 100

mRegistUser = RegistUser()
SERVER_URL = "http://ec2-13-125-111-212.ap-northeast-2.compute.amazonaws.com/download/"

usecase = UsecaseList()
usecase.setUsecase("water", ["마실", "음료", "물"], ["배식", "급여", "주다", "먹"], 60)
usecase.setUsecase("feed", ["밥", "먹", "사료", "간식", "식사","식"], ["배식", "급여", "주다", "먹"], 60)
usecase.setUsecase("open", ["문", "입구"], ["열", "오픈", "개방"], 50)
usecase.setUsecase("camera", ["사진", "상황", "모습", "얼굴", "현황"], ["보", "알", "보내"], 60)
usecase.setUsecase("regist", ["[등록]"],["[등록]"], 50)
usecase.setUsecase("information",["[정보]"],["[정보]"],50)
usecase.setUsecase("howToUse",["[사용법]","[도우미]","[도움말]"],["[사용법]","[도우미]","[도움말]"],50)

def postPiOperation(user_key,operation):
    URL, PiKey =  mRegistUser.findURLandPiKey(user_key)
    url = URL + "/" + PiKey + "/operation"
    print("Send to pi >> " + url)
    header={'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(url=url, headers = header, data=json.dumps(operation))

    mRegistUser.closeDatabase()
    return response

def getImageFileFromPiServer(user_key):
    URL, PiKey =  mRegistUser.findURLandPiKey(user_key)
    url = URL + "/" + PiKey + "/get_image"
    print("Send to pi >> " + url)
    response = requests.get(url=url, stream=True)

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

        if 'regist' in result:
            try:
                data = message.split("/")
                email = data[1]
                PiKey = data[2]

            except:
                postBodyMessage = {
                    'message': {
                        'text': "등록양식이 잘못되었습니다 :("
                    },
                    'keyboard': {
                        'type': 'text'
                    }
                }
                return postBodyMessage

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

        elif "information" in result:
            mRegistUser.openDatabase()
            sendMSG = mRegistUser.findUserEmail(user_key=user_key)
            mRegistUser.closeDatabase()

            postBodyMessage = {
                'message': {
                    'text': sendMSG
                },
                'keyboard': {
                    'type': 'text'
                }
            }
            return postBodyMessage

        elif "howToUse" in result:
            postBodyMessage = {
                'message': {
                    'text': """
아래의 사용설명서를 참고해주세요.\n
https://github.com/kuj0210/opensourceproject
"""
                },
                'keyboard': {
                    'type': 'text'
                }
            }
            return postBodyMessage

        else: #elif 'regist' not in result:
            mRegistUser.openDatabase()
            isRegistedUser = mRegistUser.checkRegistedUser(user_key)
            if isRegistedUser is True:
                operation = {}
                operation["operation"] = result
                response = postPiOperation(user_key=user_key, operation=operation)
                message = response.json()
                sendMSG = message["message"]["text"]
                isCamera = message["message"]["camera"]

                if isCamera == True:
                    mRegistUser.openDatabase()
                    print("이미지 파일 받는중...")
                    response = getImageFileFromPiServer(user_key=user_key)
                    now = time.localtime()

                    PATH = "uploaded/"
                    IMAGENAME = "Screenshot_%04d-%02d-%02d_%02d-%02d-%02d.jpg" %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

                    with open(PATH+IMAGENAME, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=2048):
                            if chunk: f.write(chunk)
                    f.close()

                    print("image making success. %s" %(PATH+IMAGENAME))

                    postBodyMessage = {
                        'message': {
                            'text': sendMSG + SERVER_URL + PATH + IMAGENAME
                        },
                        'keyboard': {
                            'type': 'text'
                        }
                    }
                    return postBodyMessage

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
