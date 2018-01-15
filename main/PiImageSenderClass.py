from requests_toolbelt import MultipartEncoder
import requests
import threading
import os

class PiImageSenderClass(threading.Thread):
    def __init__(self, operation):
        self.url = "http://localhost:8080/upload"
        self.operation = operation
        self.filename = "image/" + self.operation + ".jpg"
        self.filelink = None

    def run(self):
        if os.path.isfile(self.filename) == True:
            print("Post Server :" + self.url + ", filename : " + self.filename);
            f = open(self.filename, 'rb')
            m = MultipartEncoder({'image': (f.name, f, 'text/plain')})
            try:
                print(m.to_string())
                response = requests.post(url=self.url, data=m, headers={'Content-Type': m.content_type})
                result = response.status_code
                if result == 204:
                    self.filelink = "http://http://ec2-13-125-111-212.ap-northeast-2.compute.amazonaws.com:8080:8080/download/" + self.filename
                else:  # data["result"] == False :
                    self.filelink = "Image : None"
                return self.filelink
            except:
                print("Post is Failed, maybe Server is Down or URL is incorrect.")
                return "Imagefile Error"
        else:
            print("Imagefile is not this path...")
            return "Imagefile Error"

