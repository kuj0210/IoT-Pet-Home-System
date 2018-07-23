from . import util

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
        self.andList=['와','과','고','이랑','랑']

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
                    count+=util.GRAVITY_N
                    break
            if count>=util.GRAVITY_N:
                break
        first = count
        for verb in self.v:
            for j in range(i+1,len(sentence)):
                if verb == sentence[j]:
                    #print(verb)
                    count+=util.GRAVITY_ANY
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