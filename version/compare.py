#-*-coding: utf-8-*-

class KeyWord:
    def __init__(self,word):
        self.keyWord=word
        self.n=[]
        self.v=[]
        self.cp=0

    def setNouns(self,list):
        self.n=list
    def setVerbs(self,list):
        self.v=list
    def setCp(self,cp):
        self.cp=cp

    def isMine(self,sentence):
        count =0
        for verb in self.v:
            if verb in sentence:
                count+=50

        for noun in self.n:
            if noun in sentence:
                count+=60
        return count

    def _print(self):
        print("키워드 명칭: "+self.keyWord)
        print(self.n)
        print(self.v)
        print("")

class UsecaseList:
    def __init__(self):
        self.usecase=[]

    def setUsecase(self,name,nList,vList,cp):
        self.usecase.append(KeyWord(name))
        self.usecase[len(self.usecase)-1].setNouns(nList)
        self.usecase[len(self.usecase)-1].setVerbs(vList)
        self.usecase[len(self.usecase) - 1].setCp(cp)
    def printList(self):
        for item in self.usecase:
            item._print()


    def analyzeSentence(self,sentence):
        request =[]
        for item in self.usecase:
            if item.isMine(sentence)>=item.cp:

                request.append(item.keyWord)
        return request