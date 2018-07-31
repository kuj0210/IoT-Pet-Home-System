from ChattingBot.db import Register
from ChattingBot.nl import usecase_finder
from ChattingBot.reply import reply, exception

from ChattingBot.auth import IDissuance
from . import util, payload

class Handler:
    def __init__(self):
        self.regist = Register.Register()
        self.IDI = IDissuance.IDIssuance()

    def eventHandler(self, infomationFromNaverTalk):
        sendMSG = "None"
        user = infomationFromNaverTalk["user"]
        if infomationFromNaverTalk["event"] == util.OEPN_EVENT:
            sendMSG = reply.OPEN_MSG

        elif infomationFromNaverTalk["event"] == util.LEAVE_EVENT:
            sendMSG = reply.LEAVE_MSG

        elif infomationFromNaverTalk["event"] == util.FRIEND_EVENT:
            if infomationFromNaverTalk["state"] == "on":
                sendMSG = reply.ON_FRIEND_MSG
            else:
                self.regist.insertUserRequest(user, "UPDATE")
                sendMSG = reply.OFF_FRIEND_MSG + "\n" + self.regist.deleteUserData(user)

        elif infomationFromNaverTalk["event"] == util.ECHO_EVENT:
            return "Echo"

        elif infomationFromNaverTalk["event"] == util.SEND_EVENT \
                and infomationFromNaverTalk["typing"] == util.TYPING_TYPE:
            sendMSG = self.handlerForSendEvent(user, infomationFromNaverTalk["message"])
        else:
            sendMSG = exception.UNSUPPORTED_TYPE_COMMAND

        postBodyMessage = payload.getPostBodyMessage(user, sendMSG)
        return postBodyMessage

    def handlerForSendEvent(self,user,msg):
            #finder setting
        usecaseFinder = usecase_finder.UsecaseFinder()
        usecaseFinder.setUserSetting()
        requestlist=usecaseFinder.analyzeSentence(msg)

        if "howToUse" in requestlist:
            print("도움 ")
            smsg = reply.HOW_TO_USE
            return smsg

        elif "regist" in requestlist:
            id = self.IDI.getTempID(user)
            if self.regist.insertTempID(user, id) == False:
                return exception.REGISTERD_USER
            return util.REGIST_URL+id

        else :
            res=self.regist.insertUserRequest(user," ".join(requestlist))
            if len(requestlist) == 0:
                return exception.UNKNOWN_COMMAND

            #2 리퀘스트에 해당 시리얼 넣음
            return " ".join(requestlist)+res

    def getDataFromNaverTalk(self, dataFromMessenger):
        user = dataFromMessenger["user"]
        event = dataFromMessenger["event"]
        dicForSaveUserData = {"user": user, "event": event}

        if event != util.FRIEND_EVENT:
            dicForSaveUserData["typing"] = dataFromMessenger["textContent"]["inputType"]
            if dicForSaveUserData["typing"] == "typing":
                dicForSaveUserData["message"] = dataFromMessenger["textContent"]["text"]

        if "options" in dataFromMessenger and "set" in dataFromMessenger["options"]:
            dicForSaveUserData["state"] = dataFromMessenger["options"]["set"]

        return dicForSaveUserData

if __name__ == "__main__":
    h = Handler()
    h.eventHandler({'user':'test','event':'send',"typing":"typing","message": {"text": "안냥"
        }})

