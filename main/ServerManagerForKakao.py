'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"

* ServerManagerForKakao.py
  - This module is used to process data from the Kakao-talk platform.
  -  This module uses to Server module for managing json data.
     Specially, This module manage json data that use to send or recieve kakao server.
     ** Json data usually use HTTP(S) Protocol's body part.
'''
# -*-coding: utf-8-*-

from ServerUtility import ServerUtility
from ResponseMessage import Message

mServerUtility = ServerUtility()
responseMessage = Message()

class KakaoMessageClass :
    '''
    - This class manage kakao-talk platform operations.
    - For more complex operations, check the "ServerUtility.py" module.
    '''
    
    def __init__(self):
        self.sendMSG = "None"
        self.NOT_REGISTED = "등록되지 않은 유저입니다. 사용자 등록부터 진행해주세요."
        self.NOT_SURPPORTED = "현재 지원하지 않는 기능이예요 :("
        self.KAKAO_PLATFORM = "kakao-talk"

    def getBaseKeyboard(self):
        # This function initialize base_kakao_Keyboard_reply.
        baseKeyboard = {
            "type": "text"
        }
        return baseKeyboard

    def manageRequest(self, user_key, message, usecase):
        '''
        1. Arguement
        - user_key : To manage user information. (ex) Is registed user?) 
        - message : Text data from client.
        - usecase : Criteria to analyze device operation.
        
        2. Output : Reply body data to send client.
        
        3. Description 
        This function is performed in three steps.
        - step 1. To analyze natual sentence (from client) and seperate it down into commands to be executed on the device.
        - step 2. To send the seperated commands to device and recieve reply from the device.
        - step 3. To reply the appropriate message to client.
        '''
        result = usecase.analyzeSentence(message)
        print(result)

        # ------------ Step 1 end ------------
        
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
                
           # ------------ Step 2 end ------------

            postBodyMessage = {
                'message': {
                    'text': self.sendMSG
                },
                'keyboard': self.getBaseKeyboard()
            }
            return postBodyMessage

            # ------------ Step 3 end ------------
