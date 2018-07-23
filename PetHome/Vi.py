from observer import *
import cv2
import numpy as np
import time
import os

class Vi(Observer):

    def __init__(self,Push):
        self.reSet(Push)
        #펫수 알아오는법(펫홈관련 모든 정보는 Translator에있고 self.mPush.T.~ 로 접근가능)
        #cnt=self.mPush.T.Count
    def run(self):
        print("Vi 시작")
        while True:
            item = self.popRQ()
            if (item != False):#사진요청시 동작
                print("이미지푸쉬발생!")
                #self.mPush.insertMSG(item.user, item.msg) 일반 메세지 푸쉬 발생법
                # self.mPush.T.pushImage(item.user,[파일명] ) 이미지푸쉬발생법
                #self.mPush.T.pushImage(item.user,self.mPush.T.SERIAL + ".png" ) 이미지푸쉬발생법

            #평소에 관측모듈 실행
            # if 필요시 push
