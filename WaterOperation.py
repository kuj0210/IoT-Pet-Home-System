#import RPi.GPIO as GPIO
import time
import threading

class WaterOperation(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.pin = 12  # PWM pin num 32

        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(self.pin, GPIO.OUT)
        #self.p = GPIO.PWM(self.pin, 50)

    def run(self):
        self.p.start(0)
        try:
            #self.p.ChangeDutyCycle(18)
            time.sleep(1)
            #self.p.ChangeDutyCycle(7)
            #time.sleep(5)
            #self.p.ChangeDutyCycle(1)
            #time.sleep(4)
            #self.p.stop()
        except KeyboardInterrupt:
            self.p.stop()
            return "fail", False

        #GPIO.cleanup()
        return "success", False
