import requests, json, socket

class PiSetting:
    def __init__(self):
        self.configFile = "config-pi.txt"
        self.PiKey = ""
        self.kakaoUserList = []
        self.naverUserList = []

    def ReadConfigFile(self):
        fp = open(self.configFile,"r")

        # First line is PiKey.
        self.PiKey = fp.readline().split("\n")[0]

        # Another lines is user list(email).

        line = fp.readline()
        result = line.split("\n")[0]
        if "__kakao__" in result:
            while True:
                line = fp.readline()
                if not line: break
                email = line.split("\n")[0]
                if "__naver__" in email: break
                self.kakaoUserList.append(email)

            while True:
                line = fp.readline()
                if not line: break
                email = line.split("\n")[0]
                self.naverUserList.append(email)

        fp.close()
        print(self.kakaoUserList)
        print(self.naverUserList)

    def getPiKey(self):
        return self.PiKey

    def sendPiSettingData(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 1))
        ipAddress = s.getsockname()[0]
        url = "http://" + ipAddress + ":8888"
        postMessage = {
            "PiKey" : self.PiKey,
            "userList": {
                "kakao" : self.kakaoUserList,
                "naver" : self.naverUserList
            },
            "url": url
        }
        SERVER_URL = "https://pethome.ga:443/pi_regist"
        #SERVER_URL = "http://ec2-13-125-111-212.ap-northeast-2.compute.amazonaws.com:8080/pi_regist"
        HEADER = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url=SERVER_URL, headers=HEADER, data=json.dumps(postMessage))

        message = response.json()
        result = message["result"]
        return result
