'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
#import picamera
import time
import threading
import os

class CameraOperation(threading.Thread):
    def __init__(self):
        self.filename = "pet_Image.jpg"
        self.path = ""
        threading.Thread.__init__(self)
        self.cameraEvent = threading.Event()
        self.result = False

    def run(self):
        if not self.cameraEvent.isSet():
            dir = "image/"
            if not os.path.isdir(dir):
                os.mkdir(dir)
            try:
                self.cameraEvent.wait()
                now = time.localtime()
                self.filename = "Screenshot (%04d-%02d-%02d %02d:%02d:%02d).png"  \
                                %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

                self.path = dir + self.filename

                #camera.start_preview()
                time.sleep(1)
                #camera.capture(self.path)
                #camera.stop_preview()
                self.cameraEvent.clear()
            except:
                print("%s is not in this directory or Camera Module error." %(self.path))
                self.cameraEvent.clear()

    def removeImageFile(self):
        try:
            os.remove(self.path)
        except:
            print("%s : is not directory or in this directory." %(self.path))

    def getResult(self):
        return self.result

    def isCameraOnUnlock(self):
        return self.cameraEvent.isSet()

    def setCameraOperation(self):
        self.cameraEvent.set()

    def getFilename(self):
        return self.filename

    def getImagePath(self):
        return self.path