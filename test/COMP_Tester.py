import compare

class Tester_Comp:
    def __init__(self):
        self.usecase = compare.UsecaseList()
        #set your uscase in self.usecase.setUsecase(usecase name, nounList, VerbList, GRAVITY)
        # it will return requestList by usecase.analyzeSentence(sentence)

        self.usecase.setUsecase("water", ["마실", "음료", "물"], ["주", '주고', "주자"], compare.GRAVITY_ALL)
        self.usecase.setUsecase("feed", ["밥", "먹이", "사료", "간식", "식사", "배식"], ["주", '주고', '주자'], compare.GRAVITY_ALL)
        self.usecase.setUsecase("open", ["문", "입구"], ["열", "오픈"], compare.GRAVITY_ALL)
        self.usecase.setUsecase("camera", ["사진", "상황", "모습", "얼굴", "현황"], ["주", "주고", "주자"], compare.GRAVITY_ALL)
        self.usecase.setUsecase("regist", ["등록"], ["등록"], compare.GRAVITY_ANY)
        self.usecase.setUsecase("information", ["정보"], ["정보"], compare.GRAVITY_ANY)
        self.usecase.setUsecase("howToUse", ["사용법", '도우미', "도움말"], ["사용법", '도우미', "도움말"], compare.GRAVITY_ANY)

    def TestCOMP(self, answer,sentence):
        s1 = set(answer)
        s2 = set(self.usecase.analyzeSentence(sentence))
        if s1 == s2:
            print("OK\n")
        else:
            print("ERR\n")
    def run(self):
        # it is tester that can match answer and result
        # if you want add new Test, you add self.TestCOMP( answerList ,  Sentence)
        self.TestCOMP( ['water','feed'] ,  "밥주고 물 좀 줄 수 있니" )
        self.TestCOMP(['water','feed'],"밥이랑 물 줘")
        self.TestCOMP(['water','feed'],"밥하고 물 줘")
        self.TestCOMP(['water','feed'],"밥주면서 물도 줘")
        self.TestCOMP(['feed'],"밥주고 물은 아...아니다")
        self.TestCOMP(['feed'],"배식해줘")
        self.TestCOMP(['howToUse'],"도움말")
        self.TestCOMP(['camera'],"사진찍어줘")
        self.TestCOMP(['open'],"문열어줘")


if __name__ == '__main__':
    Tester = Tester_Comp()
    Tester.run()