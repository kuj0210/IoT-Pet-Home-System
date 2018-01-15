import RPi.GPIO as GPIO
import time
import threading

class DoorOperation(threading.Thread):
    def __init__(self):
        self.motor = 0
        self.TERM = 8
        threading.Thread.__init__(self)

    def run(self):
        self.motor.start(0)
        try:
            self.motor.ChangeDutyCycle(18)
            time.sleep(self.TERM)
            self.motor.stop()

        except KeyboardInterrupt:
            self.motor.stop()
            return "fail", False

        return "success", False

    def setPin(self, p):
        self.motor = p