'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
#import RPi.GPIO as GPIO
import time
import threading

class DoorOperation(threading.Thread):
    def __init__(self):
        self.motor = 0
        self.OPEN_TERM = 10
        self.STOP_TERM = 3
        self.CLOSE_TERM = 4
        # self.dp = GPIO.PWM(18, 50)
        # self.setPin()
        threading.Thread.__init__(self)
        self.sem_using = threading.Semaphore(1)  # 1명만 쓸것

    def run(self):
        try:
            #self.motor.start(0)
            self.sem_using.acquire()
            print("Door 시작!")
            #self.motor.ChangeDutyCycle(17)
            time.sleep(self.OPEN_TERM)
            #self.motor.ChangeDutyCycle(7)
            time.sleep(self.STOP_TERM)
            #self.motor.ChangeDutyCycle(5)
            time.sleep(self.CLOSE_TERM)
            #self.motor.stop()
            print("Door Complete")
            self.sem_using.release()

        except KeyboardInterrupt:
            print("Door operation interrupt")
            self.sem_using.release()
            #self.motor.stop()

    #def setPin(self):
    #    self.motor = self.dp