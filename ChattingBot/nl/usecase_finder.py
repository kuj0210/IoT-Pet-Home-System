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
    ##don't Touch
    def __init__(self):
        self.keyword = keyword
        self.kkma = Kkma()
        self.kkma.pos(u'성능을 위한 더미 데이터')  # this is dummy for performance
        self.usecase = []
        self.parsingNVLIST = []
        self.parsingLIST = []
        self.dic = {}

    def getNV(self, sentence):
        '''
        1. Arguement
            - sentence : it is parshed by KoNLPy

        2. Output : [nouns, verbs, ands ]

        3. Description
            this method return 'and', 'nouns', 'verb' list from sentence
        '''
        self.parsingNVLIST = []
        self.parsingLIST = []
        data = self.kkma.pos(sentence)
        # print(data)
        for list in data:
            if 'N' in list[1] or list[1].count('V') > 1 or 'C' in list[1] or 'JKM' in list[1]:
                self.parsingNVLIST.append(list[0])
                self.parsingLIST.append(list)
        print("\nkkma_LOG %s" % self.parsingNVLIST)

    ##don't Touch
    def setUserSetting(self):
        self.setUsecase("info", ["온도", "습도", "먼지", "공기", "방", "상황"], ["주", '주고', "알려주"], util.GRAVITY_ALL)
        self.setUsecase("music", ["동요", "노래"], ["재생", "틀", "들려주"], util.GRAVITY_ALL)
        self.setUsecase("voice", ["목", "소리", "목소리", "음성", "엄마", "아빠", "부모", "가족"], ["재생", "들려주"], util.GRAVITY_ALL)
        self.setUsecase("camera", ["사진", "상황", "모습", "얼굴", "현황"], ["보여주", "찍", "알려주"], util.GRAVITY_ALL)
        self.setUsecase("regist", ["등록"], ["등록"], util.GRAVITY_ANY)
        self.setUsecase("howToUse", ["사용법", '도우미', "도움말"], ["사용법", '도우미', "도움말"], util.GRAVITY_ANY)

    def printList(self):
        '''
        1. Description
            this method print all included keyword
        '''
        for item in self.usecase:
            item._print()

    def analyzeSentence(self, sentence):
        '''
        1. Arguement
            - sentence : it is sentence which you want to analyze
        2. Output : [uscases]
        3. Description
            This function search his keyword list  and return list that sentence want
        '''
        request = []
        self.getNV(sentence)
        for item in self.usecase:
            if item.isMe(self.parsingNVLIST, self.parsingLIST) == True:
                request.append(item.keyWord)

        return request

    def setUsecase(self, name, nList, vList, gravity):
        '''
        1. Arguement
            - name : KeyWord(usecase) name
            - nList : it is nouns list for Distinguish keyword
            - vList : it is verbs list for Distinguish keyword
            - gravity : it is Interest in nouns or verb

        2. Description
            This function add keyword
        '''
        self.usecase.append(self.keyword.KeyWord(name))
        keyword = self.usecase[len(self.usecase) - 1]
        keyword.setNouns(nList)
        keyword.setGravity(gravity)
        keyword.setVerbs(vList)
