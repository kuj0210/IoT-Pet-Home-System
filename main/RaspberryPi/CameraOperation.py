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
        dir = "image/"
        if not os.path.isdir(dir):
            os.mkdir(dir)

        if not self.cameraEvent.isSet():
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
                return "success"
            except:
                print("%s is not in this directory or Camera Module error." %(self.path))
                self.cameraEvent.clear()
                return "fail"

    def getFilename(self):
        return self.filename

    def getImagePath(self):
        return self.path

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
