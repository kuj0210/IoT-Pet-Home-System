import requests, json, socket

class PiSetting:
    def __init__(self):
        self.configFile = "config-pi.txt"
        self.PiKey = ""
        self.userList = []

    def ReadConfigFile(self):
        fp = open(self.configFile,"r")

        # First line is PiKey.
        self.PiKey = fp.readline().split("\n")[0]

        # Another lines is user list(email).
        while True:
            line = fp.readline()
            if not line: break
            email = line.split("\n")[0]
            self.userList.append(email)

        fp.close()

    def getPiKey(self):
        return self.PiKey

    def getUserList(self):
        return self.userList

    def sendPiSettingData(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 1))
        ipAddress = s.getsockname()[0]
        url = "http://" + ipAddress + ":8888"
        postMessage = {
            "PiKey" : self.PiKey,
            "userList": self.userList,
            "url": url
        }
        SERVER_URL = "http://ec2-13-125-111-212.ap-northeast-2.compute.amazonaws.com:8080/pi_regist"
        HEADER = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url=SERVER_URL, headers=HEADER, data=json.dumps(postMessage))

        message = response.json()
        result = message["result"]
        return result
