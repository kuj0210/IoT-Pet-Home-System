#import RPi.GPIO as GPIO
import time
import threading

class DoorOperation(threading.Thread):
    def __init__(self):
        self.motor = 0
        self.OPEN_TERM = 10
        self.STOP_TERM = 3
        self.CLOSE_TERM = 4
        threading.Thread.__init__(self)
        self.doorEvent = threading.Event()

    def run(self):
        #self.motor.start(0)
        while not self.doorEvent.isSet():
            try:
                self.doorEvent.wait()
                print("Door 시작!")
                #self.motor.ChangeDutyCycle(17)
                time.sleep(self.OPEN_TERM)
                #self.motor.ChangeDutyCycle(7)
                time.sleep(self.STOP_TERM)
                #self.motor.ChangeDutyCycle(5)
                time.sleep(self.CLOSE_TERM)
                #self.motor.stop()
                print("Door Complete")
                self.doorEvent.clear()

            except KeyboardInterrupt:
                print("Door operation interrupt")
                self.doorEvent.clear()
                #self.motor.stop()

    def setPin(self, p):
        self.motor = p

    def isDoorOnUnlock(self):
        return self.doorEvent.isSet()

    def setDoorOperation(self):
        self.doorEvent.set()
