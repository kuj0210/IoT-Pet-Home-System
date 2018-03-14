'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"

* ServerManagerForNaver.py
  - This module is used to process data from the Naver-talk-talk platform.
  -  This module uses to Server module for managing json data.
     Specially, This module manage json data that use to send or recieve naver-talk-talk server.
     ** Json data usually use HTTPS Protocol's body part.
'''
#-*-coding: utf-8-*-

from ScreenshotThread import ScreenshotThread
from ServerUtility import ServerUtility
from ResponseMessage import Message

mServerUtility = ServerUtility()
responseMessage = Message()

mScreenshotThread = ScreenshotThread()
mScreenshotThread.daemon = True
mScreenshotThread.setServerUtilityReference(mServerUtility)
mScreenshotThread.start()


def parsingPushData(message):
    '''
    1. Arguement
    - message : data from device push alarm thread.
        
    2. Output : the appropriate message to reply client
        
    3. Description
    This function analyze data that receive from device and make reply message.
    If you don't understand this data, you can check ".API_Doc/pi_push_alarm.json".
    '''
    sendMSG = "None"

    if message["fromPi"] == True:
        list = message["sensor"]["list"]

        if list == "water":
            waterPush_time = message["sensor"]["water"]["time"]
            if sendMSG == "None":
                sendMSG = "펫에게 물을 준지 %d시간이 지났어요..." %(waterPush_time)
            else :
                sendMSG += "펫에게 물을 준지 %d시간이 지났어요..." %(waterPush_time)
        else: #if sensor == "feed":
            feedPush_time = message["sensor"]["feed"]["time"]
            if sendMSG == "None":
                sendMSG = "펫에게 밥을 준지 %d시간이 지났어요..." %(feedPush_time)
            else :
                sendMSG += "펫에게 밥을 준지 %d시간이 지났어요..." %(feedPush_time)

    else: # if message["fromPi"] == False:
        sendMSG = "안녕하세요!"

    return sendMSG

class NaverMessageClass :
    '''
    - This class manage naver-talk-talk platform operations.
    - For more complex operations, check the "ServerUtility.py" module.
    '''
        
    def __init__(self):
        self.openMSG = """
                안녕하세요! IoT 펫홈 시스템입니다.
                무엇을 도와드릴까요?
                """
        self.leaveMSG = "나중에 뵈요~ :)"

        self.registErrorMSG = "등록양식이 잘못되었습니다 :("
        self.registedUserMSG = "이미 등록된 유저입니다 :("
        self.unregistKeyMSG = "등록되지 않은 키입니다. 기기 고유키를 다시 확인해주세요."
        self.successToRegistMSG = "등록이 완료되었습니다!"

        self.howToUse = """
        아래의 사용설명서를 참고해주세요.
        https://github.com/kuj0210/opensourceproject
        """

        self.unregistedUserMSG = "등록되지 않은 유저입니다. 사용자 등록부터 진행해주세요."

    def openEvent(self):
        # Get open_event_message
        return self.openMSG

    def leaveEvent(self):
        # Get leave_event_message
        return self.leaveMSG

    def sendEvent(self, user, message, usecase):
        '''
        1. Arguement
        - user : To manage user information. (ex) Is registed user?) 
        - message : Text data from client.
        - usecase : Criteria to analyze device operation.
        
        2. Output : Reply the appropriate message
        
        3. Description
        This function is performed in two steps.
        - step 1. To analyze natual sentence (from client) and seperate it down into commands to be executed on the device.
        - step 2. To send the seperated commands to device and recieve reply from the device.
        '''
        result = usecase.analyzeSentence(message)
        print(result)

        if "howToUse" in result:
            return responseMessage.inform_howToUse_Message()

        elif 'regist' in result:
            return responseMessage.regist_userMessage(
                message=message, user_key=user, mServerUtility=mServerUtility)

        elif "information" in result:
            return responseMessage.inform_userInformation_Message(user_key=user,mServerUtility=mServerUtility)

        else:  # elif 'regist' not in result:
            mServerUtility.openDB()
            isRegistedUser = mServerUtility.getDatabase().checkRegistedUser(platform="naver-talk", user_key=user)
            if isRegistedUser is True:
                operation = {}
                operation["operation"] = result
                response = mServerUtility.postPiOperation(platform="naver-talk", user_key=user, operation=operation)
                getResultByPiServer = response.json()

                sendMSG = responseMessage.operation_result_Message(
                    getResultByPiServer=getResultByPiServer, ServerUtility=ServerUtility, user_key=user)

                return sendMSG

            else:  # elif isRegistedUser is False
                return self.unregistedUserMSG

    def manageEvent(self, data, usecase):
        '''
        1. Arguement
        - data : Request's body part from Naver-talk-talk API server.
        - usecase : Criteria to analyze device operation.
        
        2. Output : Reply body data to send client.
        
        3. Description
        This function is performed in two steps.
        - step 1. To analyze data(from client) and execute the appropriate function.
        - step 2. To recieve each function's return value and make reply data.
        '''
        sendMSG = "None"
        user = data["user"]

        if data["event"] == "open":
            sendMSG = self.openEvent()

        elif data["event"] == "leave":
            sendMSG = self.leaveEvent()

        elif data["event"] == "send":
            message = data["textContent"]["text"]
            if data["textContent"]["inputType"] == "typing":
                sendMSG = self.sendEvent(user=user,message=message,usecase=usecase)
            else:
                sendMSG = "현재 지원하지 않는 타입의 메세지예요 ㅠㅠ"

        postBodyMessage = {
            "event": "send",
            "user" : user,
            "textContent": {
                "text": sendMSG
            }
        }

        return postBodyMessage

    def sendEventForPush(self, PiKey, message):
        '''
        1. Arguement
        - PiKey : Key to recognize device
        - message : Text data from push thread.

        2. Description
        This function send device status message to using device client.
        The device status message(arg:message) recieve from func::parsingPushData.
        '''
        mServerUtility.openDB()
        userlist = mServerUtility.getDatabase().getUserlist(PiKey=PiKey)
        mServerUtility.closeDB()

        sendMSG = parsingPushData(message)

        print(userlist[0])
        for user in userlist[0]:
            postPushMessage = {
                "event": "send",
                "user": user,
                "textContent": {
                    "text" : sendMSG
                }
            }
            print(postPushMessage)
            mServerUtility.postToNaverTalk(body=postPushMessage)
