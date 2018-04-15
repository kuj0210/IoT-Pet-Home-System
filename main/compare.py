'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE
- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"

* compare.py
    This module is related to analyze message. 
'''

#-*-coding: utf-8-*-
import time

from konlpy.tag import Kkma

GRAVITY_N = 60  # if it meet N list, think true
GRAVITY_ANY = 40  # if it meet N or V list  think true
GRAVITY_ALL = 100  # if it meet N or V list  think true

class KeyWord:

    def __init__(self,word):
        '''
        1. Arguement
            - word : usecase name which will be returned
        '''
        self.keyWord=word
        self.n=[]
        self.v=[]
        self.gravity=0
        self.andList=['와','과','고','이랑','']

    def setNouns(self,list):
        self.n=list
    def setVerbs(self,list):
        self.v=list
    def setGravity(self,gravity):
        self.gravity=gravity
    def isMe(self,sentence,originLIST):
        '''
        1. Arguement
            - sentence : it is parshed by KoNLPy and Collecting noun and verb
            - originLIST : it is parshed by KoNLPy

        2. Output : self.keyWord

        3. Description
            if sentence is feat this case, return self.keyWord
        '''

        count =0
        i=0
        flag = -1
        index =-1
        AND = "NODATA"
        #print(sentence)
        for noun in self.n:
            for i in range(len(sentence)):
                if noun == sentence[i]:
                    #sprint(noun)
                    count+=GRAVITY_N
                    break
            if count>=GRAVITY_N:
                break
        first = count
        for verb in self.v:
            for j in range(i+1,len(sentence)):
                if verb == sentence[j]:
                    #print(verb)
                    count+=GRAVITY_ANY
                    break
            if count>first:
                break


        for AND in self.andList:
            if AND in sentence:
                index = sentence.index(AND)
                break


        if index !=-1 and 'N' in originLIST[index-1][1]and 'N' in originLIST[index+1][1]:
            #print("TRUE")
            flag=True



        if self.gravity<=count:
            if noun in sentence:
                sentence.remove(noun)
            if verb in sentence and flag ==-1:
                sentence.remove(verb)
            if flag == True and index!=-1:
                sentence.remove(AND)


            return True


        return False
    def _print(self):
        '''
        1. Description
            print self(keyWord,n,v)
        '''
        print("키워드 명칭: "+self.keyWord)
        print(self.n)
        print(self.v)
        print("")

class UsecaseList:
    ##don't Touch
    def __init__(self):
        self.kkma = Kkma()
        self.kkma.pos(u'성능을 위한 더미 데이터')  # this is dummy for performance
        self.usecase=[]
        self.parsingNVLIST =[]
        self.parsingLIST = []
    def getNV(self,sentence):
        '''
        1. Arguement
            - sentence : it is parshed by KoNLPy

        2. Output : [nouns, verbs, ands ]

        3. Description
            this method return 'and', 'nouns', 'verb' list from sentence
        '''
        self.parsingNVLIST=[]
        self.parsingLIST=[]
        data =self.kkma.pos(sentence)
        print(data)
        #print(data)
        for list in data:
            if 'N' in list[1] or list[1].count('V')>1 or'C' in list[1]or'JKM' in list[1] :
                self.parsingNVLIST.append(list[0])
                self.parsingLIST.append(list)
        print(self.parsingNVLIST)
    ##don't Touch


    def printList(self):
        '''
        1. Description
            this method print all included keyword
        '''
        for item in self.usecase:
            item._print()


    def analyzeSentence(self,sentence):
        '''
        1. Arguement
            - sentence : it is sentence which you want to analyze
        2. Output : [uscases]
        3. Description
            This function search his keyword list  and return list that sentence want
        '''
        request =[]
        self.getNV(sentence)
        for item in self.usecase:
            if item.isMe(self.parsingNVLIST,self.parsingLIST)==True:
                request.append(item.keyWord)
        print(request)
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

        self.usecase.append(KeyWord(name))
        keyword = self.usecase[len(self.usecase) - 1]
        keyword.setNouns(nList)
        keyword.setGravity(gravity)
        keyword.setVerbs(vList)
