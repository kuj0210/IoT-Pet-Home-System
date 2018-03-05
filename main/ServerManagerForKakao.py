'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
# -*-coding: utf-8-*-
from ServerUtility import ServerUtility
from ResponseMessage import Message

#
# This module uses to Server module for managing json data.
# Specially, This module manage json data that use to send or recieve kakao server.
# ** Json data usually use HTTP(S) Protocol's body part.
#

# 동사, 명사중 아무거나 만족 : 50
# 명사 반드시 만족 : 60
# 모두 만족: 100

mServerUtility = ServerUtility()
responseMessage = Message()

class KakaoMessageClass :
    def __init__(self):
        self.sendMSG = "None"
        self.NOT_REGISTED = "등록되지 않은 유저입니다. 사용자 등록부터 진행해주세요."
        self.NOT_SURPPORTED = "현재 지원하지 않는 기능이예요 :("
        self.KAKAO_PLATFORM = "kakao-talk"

    def getBaseKeyboard(self):
        baseKeyboard = {
            "type": "text"
        }
        return baseKeyboard

    def manageRequest(self, user_key, message, usecase):
        result = usecase.analyzeSentence(message)
        print(result)

        if 'regist' in result:
            self.sendMSG = \
                responseMessage.regist_userMessage(message=message,user_key=user_key,mServerUtility=mServerUtility)

        elif "information" in result:
            self.sendMSG = \
                responseMessage\
                    .inform_userInformation_Message(user_key=user_key, mServerUtility=mServerUtility)

        elif "howToUse" in result:
            self.sendMSG = responseMessage.inform_howToUse_Message()

        else: #elif 'regist' not in result:
            mServerUtility.openDB()
            isRegistedUser = mServerUtility.getDatabase().checkRegistedUser(platform=self.KAKAO_PLATFORM, user_key=user_key)

            if isRegistedUser is True:
                operation = {}
                operation["operation"] = result
                response = mServerUtility.postPiOperation(platform=self.KAKAO_PLATFORM, user_key=user_key, operation=operation)
                getResultByPiServer = response.json()

                sendMSG = responseMessage\
                    .operation_result_Message(
                    getResultByPiServer=getResultByPiServer, ServerUtility=mServerUtility, user_key=user_key)

                if self.sendMSG == "None" :
                    self.sendMSG = self.NOT_SURPPORTED

            else: # elif isRegistedUser is False
                self.sendMSG = self.NOT_REGISTED

            postBodyMessage = {
                'message': {
                    'text': self.sendMSG
                },
                'keyboard': self.getBaseKeyboard()
            }
            return postBodyMessage
