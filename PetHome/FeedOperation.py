'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
#import RPi.GPIO as GPIO
import time
import threading
import os

class FeedOperation():
    def __init__(self):
        self.motor = 0
        self.OPEN_TERM = 0.4
        self.CLOSE_TERM = 1
        #self.fp = GPIO.PWM(19, 50)
        #self.setPin()

    def run(self):
        try:
            print("Feed 시작!")
            #self.motor.start(0)
            #self.motor.ChangeDutyCycle(3)
            time.sleep(self.OPEN_TERM)
            #self.motor.ChangeDutyCycle(6)
            time.sleep(self.CLOSE_TERM)
            #self.motor.stop()
            print("Feed Complete")

        except KeyboardInterrupt:
            print("Feed operation interrupt")
            #self.motor.stop()

    #def setPin(self):
    #    self.motor = self.fp

