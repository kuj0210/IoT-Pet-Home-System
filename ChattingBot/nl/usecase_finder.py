'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE
- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"

* compare.py
    This module is related to analyze message.
'''

# -*-coding: utf-8-*-
import time
from . import util, keyword
from konlpy.tag import Kkma

class UsecaseFinder:
    def __init__(self):
        self.keyword = keyword
        self.kkma = Kkma()
        self.kkma.pos(u'성능을 위한 더미 데이터')  # this is dummy for performance
        self.usecase = []
        self.parsingNVLIST = []
        self.parsingLIST = []
        self.dic = {}

    def getNV(self, sentence):
        self.parsingNVLIST = []
        self.parsingLIST = []
        data = self.kkma.pos(sentence)
        # print(data)
        for list in data:
            if 'N' in list[1] or list[1].count('V') > 1 or 'C' in list[1] or 'JKM' in list[1]:
                self.parsingNVLIST.append(list[0])
                self.parsingLIST.append(list)
        print("\nkkma_LOG %s" % self.parsingNVLIST)

    def setUserSetting(self):
        self.setUsecase("feed", ["먹이","사료","먹을 것","밥","배식"], ["주","줘","급여","배식","먹"], util.GRAVITY_N)
        self.setUsecase("open", ["문","입구"], ["열","오픈","개방"], util.GRAVITY_N)
        self.setUsecase("camera", ["사진", "상황", "모습", "얼굴", "현황"], ["보여주", "찍", "알리"], util.GRAVITY_ALL)
        self.setUsecase("regist", ["등록"], ["등록"], util.GRAVITY_ANY)
        self.setUsecase("howToUse", ["사용법", '도우미', "도움말"], ["사용법", '도우미', "도움말"], util.GRAVITY_ANY)

    def printList(self):
        for item in self.usecase:
            item._print()

    def analyzeSentence(self, sentence):
        request = []
        self.getNV(sentence)
        for item in self.usecase:
            if item.isMe(self.parsingNVLIST, self.parsingLIST) == True:
                request.append(item.keyWord)

        return request

    def setUsecase(self, name, nList, vList, gravity):
        self.usecase.append(self.keyword.KeyWord(name))
        keyword = self.usecase[len(self.usecase) - 1]
        keyword.setNouns(nList)
        keyword.setGravity(gravity)
        keyword.setGravity(gravity)
        keyword.setVerbs(vList)
