import RPi.GPIO as GPIO
import time
import threading

class WaterOperation(threading.Thread):
    def __init__(self):
        self.motor = 0
        self.OPEN_TERM = 0.2
        self.STOP_TERM = 3
        self.CLOSE_TERM = 0.2
        threading.Thread.__init__(self)

    def run(self):
        #self.p.start(0)
        try:
            self.motor.ChangeDutyCycle(8)
            time.sleep(self.OPEN_TERM)
            self.motor.ChangeDutyCycle(6.8)
            time.sleep(self.STOP_TERM)
            self.motor.ChangeDutyCycle(5)
            time.sleep(self.CLOSE_TERM)
            self.motor.stop()
        except KeyboardInterrupt:
            self.motor.stop()
            return "fail", False

        return "success", False

    def setPin(self, p):
        self.motor = p
