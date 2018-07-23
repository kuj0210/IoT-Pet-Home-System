import time
from push import *

class MobileSystem:
    def __init__(self):
        self.T = Translator()
        self.Push = Push()
        self.CONFIG = "configPI.txt"
        #시스템 정보

        #값 초기화
        if self.loadSerail() ==False:
            exit()
        self.bootUp()
        print("프로그램 안전부팅 완료")
    def parshResponseByNL(self,res):
        res =res.split("\n")
        res.pop()
        for i in range(len(res)):
            res[i]=res[i].strip()
        return res
    def parshResponseBySP(self,res):
        res =res.split(" ")
        return res
    def loadSerail(self):
        try:
            with open(self.CONFIG, "r") as f:
                Translator.SERIAL=f.readline()
                return True
        except:
            print("파일 입출력 에러")
            return False
        return False
    def bootUp(self):
        res=self.T.sendMsg(self.T.BOOT_URL,"NO_USER",Translator.SERIAL)
        item =self.parshResponseByNL(res)
        print(item)
        petCNT = item.pop(0)
        Translator.userList=item
        Translator.Count = int(petCNT)
    def getRequest(self,wating):
        time.sleep(wating)
        res = self.T.sendMsg(self.T.RQST_URL,"NO_USER",Translator.SERIAL)
        if 'NO' in res:
            return False
        res =self.parshResponseByNL(res)
        list =[]
        for item in res:
            atom = self.parshResponseBySP(item)
            atom.pop(0)
            list.append(atom)
        return list
    def runMobile(self):
        try:
            print("프로그램 시작합니다.")
            self.Push.PushTh.start()
        except:
            print("시작 에러")
            return

        while (True):
            try:
                list = self.getRequest(1)
                if list == False:
                    continue
                else:
                    print(list)
                    #str =""
                    while(len(list)>0):
                        item = list.pop(0)
                        user = item.pop(0)
                        print(user+"가")
                        print(item)
                        if 'UPDATE' in item:
                            print("유저변동발생!")
                            self.bootUp()

                        if 'open'in item:
                            print("문요청")
                            #str+=문요청완료\n
                        if 'feed'in item:
                            print("밥요청")
                            # str+=밥요청완료\n
                        if 'camera' in item:
                            print("카메라요청")
                            self.Push.observerList[Push.VI].insertRQ(user, "비디오스레드::사진기능완료")  # 사진기능 요청
                    # self.mPush.insertMSG(user, str) 일반 메세지 푸쉬 발생법

            except:
                print("runMobile 리퀘스트 전송 에러")


if __name__ =="__main__":
    MS=MobileSystem()
    MS.runMobile()

