from ChattingBot.api.config import url

PUSH_URL = "https://gw.talk.naver.com/chatbot/v1/event"
UPDATE_URL = "https://gw.talk.naver.com/chatbot/v1/imageUpload HTTP/1.1"

IMAGE_URL = url.SERVER_URL + 'download/'
REGIST_URL = url.SERVER_URL + 'signup/'

OEPN_EVENT = "open"
LEAVE_EVENT = "leave"
FRIEND_EVENT = "friend"
ECHO_EVENT = "echo"
SEND_EVENT = "send"
TYPING_TYPE = "typing"

def getSerial(str):
    return str.split(':')[1].replace(' ', '')