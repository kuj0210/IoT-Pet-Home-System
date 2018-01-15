import RPi.GPIO as GPIO
import time
import threading
import os

class WaterOperation(threading.Thread):
    def __init__(self):
        self.motor = 0
        self.OPEN_TERM = 1
        self.STOP_TERM = 5
        self.CLOSE_TERM = 1
        threading.Tread.__init__(self)

    def run(self):
        #self.p.start(0)
        try:
            self.motor.ChangeDutyCycle(18)
            time.sleep(self.OPEN_TERM)
            self.motor.ChangeDutyCycle(7)
            time.sleep(self.STOP_TERM)
            self.motor.ChangeDutyCycle(self.CLOSE_TERM)
            self.motor.stop()
        except KeyboardInterrupt:
            self.motor.stop()
            return "fail", False

        return "success", False

    def setPin(self, p):
        self.motor = p
        
