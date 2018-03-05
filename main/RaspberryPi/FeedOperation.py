import RPi.GPIO as GPIO
import time
import threading
import os

class FeedOperation(threading.Thread):
    def __init__(self):
        self.motor = 0
        self.OPEN_TERM = 0.4
        self.CLOSE_TERM = 1
        self.FEED_DONE = "FEED_DONE"
        threading.Thread.__init__(self)
        self.feedEvent = threading.Event()
        self.sem = threading.Semaphore(1)

    def run(self):
        self.motor.start(0)
        while not self.feedEvent.isSet():
            try:
                self.feedEvent.wait()
                print("Feed 시작!")
                self.motor.ChangeDutyCycle(3)
                time.sleep(self.OPEN_TERM)
                self.motor.ChangeDutyCycle(6)
                time.sleep(self.CLOSE_TERM)
                self.motor.stop()
                print("Feed Complete")
                os.environ["PUSH"] = "FEED"

                self.feedEvent.clear()

            except KeyboardInterrupt:
                print("Feed operation interrupt")
                self.feedEvent.clear()
                self.motor.stop()

    def setPin(self, p):
        self.motor = p

    def isFeedOnUnlock(self):
        return self.feedEvent.isSet()

    def setFeedOperation(self):
        self.feedEvent.set()

