import unittest
from ChattingBot.nl.usecase_finder import UsecaseFinder

nl = UsecaseFinder()
nl.setUserSetting()

def TestCompare(answer, sentence):
    s1 = set(answer)
    s2 = set(nl.analyzeSentence(sentence))
    if s1 == s2:
       return True
    else:
        return False

class nl_test(unittest.TestCase):
    def test_feed(self):
        c1 = nl.analyzeSentence("밥 주세요.")
        c2 = nl.analyzeSentence("먹이 줄래?")
        self.assertEqual(["feed"],c1)
        self.assertEqual(["feed"],c2)

    def test_door(self):
        c1 = nl.analyzeSentence("문 좀 열어주세요")
        c2 = nl.analyzeSentence("문열어")
        self.assertEqual(["open"], c1)
        self.assertEqual(["open"], c2)

    def test_camera(self):
        c1 = nl.analyzeSentence("사진 좀 찍어주세요!")
        c2 = nl.analyzeSentence("현황 좀 알려주라")
        self.assertEqual(["camera"], c1)
        self.assertEqual(["camera"], c2)

    def test_all(self):
        self.assertTrue(TestCompare( ['feed'] , "밥 좀 줄 수 있니"))
        self.assertTrue(TestCompare(['feed', 'camera'],"밥주고 사진 찍어줘"))
        self.assertTrue(TestCompare(['feed'],"배식해줘"))
        self.assertTrue(TestCompare(['howToUse'],"도움말"))
        self.assertTrue(TestCompare(['camera'],"사진 찍어줘"))
        self.assertTrue(TestCompare(['open'],"문 열어줘"))
        self.assertTrue(TestCompare(['open', 'camera'], "문 열고 사진 찍어"))

if __name__ == "__main__":
    unittest.main()
