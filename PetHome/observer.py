import time
import threading

class Request:
    def __init__(self,u,m):
        self.user=u
        self.msg=m

class Observer(object):
    def __init__(self,push):
        self.mRQList =[]
        self.mPush =push
        self.sem_using = threading.Semaphore(1)  # 1명만 쓸것

    def reSet(self,push):
        self.mRQList =[]
        self.mPush =push
        self.sem_using = threading.Semaphore(1)

    def run(self):
        while(True):
            if(True): #이탈 시
                time.sleep(2)
                self.mPush.insertMSG("-----------------옵저버 스레드")

    def insertRQ(self,user,msg):
        self.sem_using.acquire()
        self.mRQList.append(Request(user,msg))
        self.sem_using.release()
    def popRQ(self):
        self.sem_using.acquire()
        if len(self.mRQList)==0:
            self.sem_using.release()
            return False
        rq = self.mRQList.pop(0)
        self.sem_using.release()
        return rq