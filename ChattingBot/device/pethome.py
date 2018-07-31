from ChattingBot.db.Register import Register
from ChattingBot.api import sender, util

class Pethome:
    def __init__(self):
        self.regist = Register()

    def bootUp(self, request):
        dataFromMessenger = request.get_json()
        serial = dataFromMessenger['textContent']['text']

        user_key = self.regist.getUserFromSerial(serial)
        pet_count = self.regist.getPetCountFromSerial(serial)
        UK = str(pet_count) + '\n' + user_key
        return UK

    def push(self, request):
        dataFromMessenger = request.get_json()  # get json data from naver talk talk
        user = dataFromMessenger['user']
        msg = dataFromMessenger['textContent']['text']

        pet_name = self.regist.getPetName(user)
        msg = pet_name + "에서 알려드립니다." + msg
        sender.sendPush(util.PUSH_URL, user, msg)
        return "True"

    def sendRequest(self, request):
        dataFromMessenger = request.get_json()  # ge/home/test"t json data from naver talk talk
        SR = dataFromMessenger['textContent']['text']

        rq = self.regist.fetchRequest(SR)
        if rq == False:
            return "NO"
        return rq