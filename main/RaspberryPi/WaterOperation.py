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

class WaterOperation(threading.Thread):
    def __init__(self):
        self.motor = 0
        self.OPEN_TERM = 0.2
        self.STOP_TERM = 3
        self.CLOSE_TERM = 0.2
        self.WATER_DONE = "WATER_DONE"
        threading.Thread.__init__(self)
        self.waterEvent = threading.Event()

    def run(self):

        while not self.waterEvent.isSet():
            try:
                #self.waterEvent.wait()
                print("Water 시작!")
                # self.p.start(0)
                #self.motor.ChangeDutyCycle(8)
                time.sleep(self.OPEN_TERM)
                #self.motor.ChangeDutyCycle(6.8)
                time.sleep(self.STOP_TERM)
                #self.motor.ChangeDutyCycle(5)
                time.sleep(self.CLOSE_TERM)
                #self.motor.stop()
                print("Water Complete")

                os.environ["PUSH"] = "WATER"
                self.waterEvent.clear()

            except KeyboardInterrupt:
                print("Water operation interrupt")
                self.waterEvent.clear()
                #self.motor.stop()

    def setPin(self, p):
        self.motor = p

    def isWaterOnUnlock(self):
        return self.waterEvent.isSet()

    def setWaterOperation(self):
        self.waterEvent.set()