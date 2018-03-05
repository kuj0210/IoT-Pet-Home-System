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
        print("Setting >> PiKey = %s" %(self.PiKey))

        # Another lines is user list(email).
        while True:
            line = fp.readline()
            if not line: break
            email = line.split("\n")[0]
            self.userList.append(email)

        print("Setting >> User list...")
        fp.close()

    def getPiKey(self):
        return self.PiKey

    def getUserList(self):
        return self.userList

    def sendPiSettingData(self):
        url = "http://" + socket.gethostbyname(socket.gethostname()) + ":8888"
        postMessage = {
            "PiKey" : self.PiKey,
            "userList": self.userList,
            "url": url
        }
        SERVER_URL = "http://localhost:8080/pi_regist"
        HEADER = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(url=SERVER_URL, headers=HEADER, data=json.dumps(postMessage))

        print("Setting >> Sending Pi settings to server...")

        message = response.json()
        result = message["result"]
        return result
