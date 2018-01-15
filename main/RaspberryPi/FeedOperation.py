import RPi.GPIO as GPIO
import time
import threading

class FeedOperation(threading.Thread):
    def __init__(self):
        self.motor = 0
        self.OPEN_TERM = 0.4
        self.CLOSE_TERM = 1
        threading.Thread.__init__(self)

    def run(self):
        self.motor.start(0)
        try:
            self.motor.ChangeDutyCycle(3)
            time.sleep(self.OPEN_TERM)
            self.motor.ChangeDutyCycle(6)
            time.sleep(self.CLOSE_TERM)
            self.motor.stop()
        except KeyboardInterrupt:
            self.motor.stop()
            return "fail", False

        return "success", False

    def setPin(self, p):
        self.motor = p
