import socket, threading


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
        txt=msg.split("\n\n")[1]
        print("["+txt+"]")
        return txt

    def attachHeader(self,type,body):
        httpString="HTTP / 1.1 200 OK\n"
        httpString+="Host: PetHouse: 8080\n"
        httpString+='''Accept: /
User - Agent: KakaoTalk / Bot2.0
Via: 1.1ghost491(squid / 3.1.23)
X - Forwarded - For: unknown
Cache - Control: max - age = 259200\n'''
        httpString+="Content-Length: %d\n"%(len(body))
        httpString+="Content-Type: %s\n"%(type)
        httpString+="Connection: keep - alive\n\n"
        httpString +=body
        return httpString



    def parshMSG(self,msg,URI):
        item = msg.split('/')
        URI.append(item[0])
        URI.append(item[1])
        parameter = None
        if len(item) == 3:
            URI.append(item[2].split('?'))
            self.argsCount = len(self.URI[2])
        self.URICount = len(self.URI)
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

        self.csocket.send(bytes(self.attachHeader("text/html",txt), 'UTF-8'))

    def processGET(self):
        if self.URI[1] is "vedio":
            self.csocket.send(bytes("you can see your pet", 'UTF-8'))

    #워커
    def run(self):
        print("Connection from : ", clientAddress)
        data = self.csocket.recv(2048)
        msg = data.decode()
        try:
            self.parshMSG(self.detachHeader(msg),self.URI)
            if self.URI[0]=="POST":
                self.processPOST()
            elif self.URI[0]=="GET":
                self.processGET()
            else:
                self.csocket.send(bytes(self.attachHeader("text/html","Not Define Method"), 'UTF-8'))
        except:
            self.csocket.send(bytes("ERR!! plz, send requst like Method/requset/parameter=x?....", 'UTF-8'))



#main함수 내용
LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")


while True:
    server.listen(5)
    clientsock, clientAddress = server.accept()  #커넥션
    newthread = ClientThread(clientAddress, clientsock) #새로운 스레드 생성
    newthread.start()# 실행
