from Vi import *
from Translator import *

class Push():
    VI = 0

    def __init__(self):
        self.T = Translator()
        self.sem_using = threading.Semaphore(1) # 1명만 쓸것
        self.sem_emp = threading.Semaphore(0) # 처음 큐는 비어있음
        self.Q=[]
        self.observerList=[]
        self.thList = []
        self.setUpObserverList()
        self.setUpThread()
        self.PushTh=threading.Thread(target = self.run)

    def setUpObserverList(self):
        self.observerList.append(Vi(self))

    def setUpThread(self):
        for ob in self.observerList:
            self.thList.append(threading.Thread(target=ob.run))

    def insertMSG(self,user,str):
        self.sem_using.acquire() # 사용을 알림
        self.Q.append(Request(user,str))
        self.sem_using.release() # 다썻다 알림
        self.sem_emp.release() # 세마포어 값 증가, 비어있던 큐에 1개들어갓음 알림

    def getMSG(self):
        self.sem_emp.acquire() # 비어있으면 대기
        self.sem_using.acquire() # 쓴다고 알림
        msg =self.Q[0]
        del self.Q[0]
        self.sem_using.release() # 다
        return msg

    def startTh(self):
        for th in self.thList:
            th.start()

    def run(self):
        self.startTh()
        cunt= 0
        while(True):
            print("PUSH-락진입")
            msg = self.getMSG()
            print("PUSH-락해제")
            if msg.user =="ALL":
                self.T.pushToAllUser(msg.msg)
            else:
                self.T.pushToUser(msg.user,msg.msg)

if __name__ == "__main__":
    p=Push()
    p.PushTh.run()