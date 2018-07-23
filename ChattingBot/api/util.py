PUSH_URL = "https://gw.talk.naver.com/chatbot/v1/event"
UPDATE_URL = "https://gw.talk.naver.com/chatbot/v1/imageUpload HTTP/1.1"

SERVER_URL = 'https://kit-iot-system.tk:443/'
IMAGE_URL = SERVER_URL + 'download/'
REGIST_URL = SERVER_URL+'signup/'

OEPN_EVENT = "open"
LEAVE_EVENT = "leave"
FRIEND_EVENT = "friend"
ECHO_EVENT = "echo"
SEND_EVENT = "send"
TYPING_TYPE = "typing"

def getSerial(self, str):
    print(str)
    return str.split(':')[1].replace(' ', '')