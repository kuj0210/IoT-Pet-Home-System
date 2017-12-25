import socket, threading
import json
import urllib

baseKeyboard = {
    "type":"text"
}

feedMessage = {
    'message':{
        'text':'우리 애완용에게 밥을 주고 있어요.'
    },
    'keyboard':{
        'type':'text'
    }
}

waterMessage = {
    'message':{
        'text':'우리 애완용에게 물을 주고 있어요.'
    },
    'keyboard':{
        'type':'text'
    }
}

doorMessage = {
    'message':{
        'text':'애완용 집 문을 열어줍니다 :)'
    },
    'keyboard':{
        'type':'text'
    }
}

cameraMessage = {
    'message':{
        'text':'사진을 찍었어요!',
        'photo':'/photo/pet.png',
        'width':640,
        'height':480
    },
    'keyboard':{
        'type':'text'
    }
}

## ----------------------------------- json data -------

class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress=clientAddress
        self.URI = []
        self.argsCount= -1
        self.URICount= -1

    def detachHeader(self,msg):
        print("[받은메세지]")
        print(msg)
        print("[/받은메세지]")
        txt=msg.split("\r\n\r\n")[1]
        if txt !=  '':
            print("["+txt+"]")
        return txt

    def attachHeader(self,type,body):
        httpString="GET https://ybot.kakao.com:443 HTTP/1.1\r\n"
        httpString+="Content-Length: %d\r\n"%(len(body))
        httpString+="Content-Type: %s\r\n"%(type)
        httpString+="Connection: keep - alive\r\n\r\n"
        httpString += body
        return httpString

    def parshMSG(self,msg,body,URI):
        item = msg.split(' /')
        URI.append(item[0])
        URI.append((item[1].split(' '))[0])
        parameter = None
        print(URI)

    def processPOST(self):
        txt=""
        if self.URICount is 3:
            if self.argsCount is 1 and self.URI[1] is "feed":
                txt="your pet get food from you"
            elif self.argsCount is 2 and self.URI[1] is "door":
                txt="your door open/close"
            else:  # ERR
                txt="Can not match argument"
        elif self.URI[1] == "voice":
            txt="you can speak to your pet"
        else:
            txt="plz, send requst like POST/requset/parameter=x?...."

        self.csocket.send(bytes(self.attachHeader("application/json; charset=utf-8",txt), 'UTF-8'))

    def processGET(self):
        if self.URI[1]=="video":
            self.csocket.send(bytes("you can see your pet", 'utf-8'))
        elif self.URI[1]=="keyboard":
            txt = json.dumps(baseKeyboard)
            #data = self.attachHeader("application/json; charset=utf-8", txt)
            #print("[보내는 메세지]")
            #print(data)
            #print("[/보내는 메세지]")
            #self.csocket.send(data.encode())

    #워커
    def run(self):
        print("Connection from : ", clientAddress)
        data = self.csocket.recv(2048)
        msg = data.decode()
        try:
            self.parshMSG(msg, self.detachHeader(msg), self.URI)
            if self.URI[0]=="POST":
                self.processPOST()
            elif self.URI[0]=="GET":
                self.processGET()
            else:
                self.csocket.send(bytes(self.attachHeader("text/html","Not Define Method"), 'UTF-8'))
        except:
            self.csocket.send(bytes("ERR!! plz, send requst like Method/requset/parameter=x?....", 'UTF-8'))

#main함수 내용
LOCALHOST = ""
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")


while True:
    server.listen(20)
    clientsock, clientAddress = server.accept()  #커넥션
    newthread = ClientThread(clientAddress, clientsock) #새로운 스레드 생성
    newthread.start()# 실행