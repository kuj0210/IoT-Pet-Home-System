#-*-coding: utf-8-*-

from compare import UsecaseList
from ResponseMessage import Message
from ServerUtility import ServerUtility
import time

# 동사, 명사중 아무거나 만족 : 50
# 명사 반드시 만족 : 60
# 모두 만족: 100

mServerUtility = ServerUtility()
responseMessage = Message()
SERVER_URL = "http://localhost:8080/download/"

usecase = UsecaseList()
usecase.setUsecase("water", ["마실", "음료", "물"], ["배식", "급여", "주다", "먹"], 60)
usecase.setUsecase("feed", ["밥", "먹", "사료", "간식", "식사","식"], ["배식", "급여", "주다", "먹"], 60)
usecase.setUsecase("door", ["문", "입구"], ["열", "오픈", "개방"], 50)
usecase.setUsecase("camera", ["사진", "상황", "모습", "얼굴", "현황"], ["보", "알", "보내"], 60)
usecase.setUsecase("regist", ["[등록]"],["[등록]"], 50)
usecase.setUsecase("information",["[정보]"],["[정보]"],50)
usecase.setUsecase("howToUse",["[사용법]","[도우미]","[도움말]"],["[사용법]","[도우미]","[도움말]"],50)

def parsingPushData(message):
    """Push data type
    {
        "PiKey" : PiKey
        "message" : {
            "fromPi" : True|False
            "sensor" : {
                "list" : {"water","feed"}
                "water" : {
                    "time" : 1
                }
                "feed" : {
                    "time" : 2
                }
            }
            "non-sensor" : {
                "sendMSG" : "sendMSG"
            }
        }
    }
    """

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
        return self.openMSG

    def leaveEvent(self):
        return self.leaveMSG

    def sendEvent(self, user, message):

        result = usecase.analyzeSentence(message)
        print(result)

        if "howToUse" in result:
            return self.howToUse

        elif 'regist' in result:
            try:
                data = message.split("/")
                email = data[1]
                PiKey = data[2]

            except:
                return self.registErrorMSG

            mServerUtility.openDB()
            regist_result = mServerUtility.getDatabase().insertUserData(platform="naver-talk", user_key=user, email=email, PiKey=PiKey)
            mServerUtility.closeDB()

            if regist_result == "등록된 유저":
                return self.registedUserMSG

            elif regist_result == "등록되지 않은 키":
                return self.unregistKeyMSG

            else:  # regist_result == "등록 완료"
                return self.successToRegistMSG

        elif "information" in result:
            mServerUtility.openDB()
            resultToFindUserEmail = mServerUtility.getDatabase().findUserEmail(platform="naver-talk", user_key=user)
            mServerUtility.openDB()

            return resultToFindUserEmail

        else:  # elif 'regist' not in result:
            mServerUtility.openDB()
            isRegistedUser = mServerUtility.getDatabase().checkRegistedUser(platform="naver-talk", user_key=user)
            if isRegistedUser is True:
                operation = {}
                operation["operation"] = result
                response = mServerUtility.postPiOperation(platform="naver-talk", user_key=user, operation=operation)
                getResultByPiServer = response.json()
                sendMSG = "None"

                if getResultByPiServer["water"] == "use":
                    if sendMSG == "None":
                        sendMSG = responseMessage.getContinueWaterMessage()
                    else:
                        sendMSG += "\n" + responseMessage.getContinueWaterMessage()
                elif getResultByPiServer["water"] == "using":
                    if sendMSG == "None":
                        sendMSG = responseMessage.getFailWaterMessage()
                    else:
                        sendMSG += "\n" + responseMessage.getFailWaterMessage()

                if getResultByPiServer["feed"] == "use":
                    if sendMSG == "None":
                        sendMSG = responseMessage.getContinueFeedMessage()
                    else:
                        sendMSG += "\n" + responseMessage.getContinueFeedMessage()
                elif getResultByPiServer["feed"] == "using":
                    if sendMSG == "None":
                        sendMSG = responseMessage.getFailFeedMessage()
                    else:
                        sendMSG += "\n" + responseMessage.getFailFeedMessage()

                if getResultByPiServer["door"] == "use":
                    if sendMSG == "None":
                        sendMSG = responseMessage.getContinueDoorMessage()
                    else:
                        sendMSG += "\n" + responseMessage.getContinueDoorMessage()
                elif getResultByPiServer["door"] == "using":
                    if sendMSG == "None":
                        sendMSG = responseMessage.getFailDoorMessage()
                    else:
                        sendMSG += "\n" + responseMessage.getFailDoorMessage()

                if getResultByPiServer["camera"] == "use":
                    # mRegistUser.openDatabase()
                    # print("이미지 파일 받는중...")
                    # response = getImageFileFromPiServer(user_key=user_key)
                    # now = time.localtime()

                    # PATH = "upload/"
                    # IMAGENAME = "Screenshot_%04d-%02d-%02d_%02d-%02d-%02d.jpg" %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

                    # with open(PATH+IMAGENAME, 'wb') as f:
                    #    for chunk in response.iter_content(chunk_size=2048):
                    #        if chunk: f.write(chunk)
                    # f.close()

                    # print("image making success. %s" %(PATH+IMAGENAME))
                    if sendMSG == "None":
                        sendMSG = responseMessage.getSuccessCameraMessage()
                    else:
                        sendMSG += responseMessage.getSuccessCameraMessage()
                        sendMSG += SERVER_URL + "upload/Screenshot_2018-01-16_02-37-14.jpg"

                elif getResultByPiServer["camera"] == "using":
                    if sendMSG == "None":
                        sendMSG = responseMessage.getFailCameraMessage()
                    else:
                        sendMSG += "\n" + responseMessage.getFailCameraMessage()

                if sendMSG == "None":
                    sendMSG = "현재 지원하지 않는 기능이예요 :("

                return sendMSG

            else:  # elif isRegistedUser is False
                return self.unregistedUserMSG

    def manageEvent(self, data):
        sendMSG = "None"
        user = data["user"]

        if data["event"] == "open":
            sendMSG = self.openEvent()

        elif data["event"] == "leave":
            sendMSG = self.leaveEvent()

        elif data["event"] == "send":
            message = data["textContent"]["text"]
            if data["textContent"]["inputType"] == "typing":
                sendMSG = self.sendEvent(user=user,message=message)
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

    def sendEventForPush(self,PiKey, message):
        mServerUtility.openDB()
        userlist = mServerUtility.getDatabase().getUserlist(PiKey=PiKey)
        mServerUtility.closeDB()

        sendMSG = parsingPushData(message)

        for user in userlist:
            print(userlist)
            for u in user:
                postPushMessage = {
                    "event": "send",
                    "user": u,
                    "textContent": {
                        "text" : sendMSG
                    }
                }
                print(postPushMessage)
                mServerUtility.postToNaverTalk(body=postPushMessage)