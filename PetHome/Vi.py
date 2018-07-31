from observer import *
import numpy as np
import imutils
import cv2
import signal
import sys
from collections import Counter
import time

class Vi(Observer):
    def __init__(self, Push):
        self.reSet(Push)
        self.width = 0
        self.height = 0
        self.area = []  # 영역별 점의 수
        self.petArea = []  # 펫의 추정위치
        self.nestArea = []  # 펫의 주 위치
        self.nestAreaFrequency = []  # 펫의 주 위치에서 누적 점의 수
        self.maxIndex = 0
        self.startTimer = 0
        self.frame = None
        self.cap = None
        self.petAreaCollection = []  # 펫의 추정위치 모음
        self.modes = []  # 최빈위치 리스트
        self.termTimer = 100 # 측정 프레임 단위            #주석 임시값 100넣음 1000넣을 예정
        self.petCount =self.mPush.T.Count  # 펫의 수
        self.wrongPetCount = 0 #잘못된 펫의 추정수
        self.modelNumber = self.mPush.T.SERIAL
        self.imageDirectory = "images/"

        self.previousTime = time.localtime(0) # 이전 PUSH시간
        self.currentTime = time.localtime() # 현재시간
        self.intervalTime = 60 # 이전 PUSH시간과 다음PUSH시간의 간격 (분 단위)
        self.gapTime = self.intervalTime + 1 # 이전 PUSH시간과 현재시간의 차이 (분 단위)

        for i in range(0, self.petCount):
            self.petArea.append(0)
        self.row = 2
        self.col = 4
        for i in range(0, self.row * self.col):
            self.area.append(0)

        self.register_all_signal()
    def run(self):
        print ("Vi시작")
        self.petTracking()

    def petTracking(self):
        try:
            print('Camera operate')
            self.cap = cv2.VideoCapture(0) #주석 0으로 변경해야함
            self.width = self.cap.get(3)
            self.height = self.cap.get(4)
            ret, frame1 = self.cap.read()
            prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            hsv = np.zeros_like(frame1)
            hsv[..., 1] = 255
        except:
            print('Camera failed to operate')
            return


        while True:
            item = self.popRQ()
            ret, self.frame = self.cap.read()

            if not ret:
                print('Video error')
                break

            if (item != False):
                print("이미지푸쉬발생!")
                self.capture()
                self.mPush.T.pushImage(item.user, self.imageDirectory + self.mPush.T.SERIAL + ".png")

            self.currentTime = time.localtime() #현재시간 갱신
            if self.previousTime != time.localtime(0):
                self.gapTime = (self.currentTime.tm_hour - self.previousTime.tm_hour) * 60\
                               + (self.currentTime.tm_min - self.previousTime.tm_min)



            self.startTimer = (self.startTimer + 1)%(self.termTimer)

            cv2.imshow('video2', self.frame)


            prvs, hsv, bgr = self.optFlow(self.frame, prvs, hsv)
            self.getCenterOfContour(bgr)
            if self.startTimer%self.termTimer == self.termTimer - 1:
                self.modes = self.modeFinder(self.petAreaCollection)
                if self.nestArea == []:
                    for i in range(0, self.petCount):
                        self.nestArea.append(self.modes[i][0])
                        self.nestAreaFrequency.append(self.modes[i][1])

                else:
                    for i in range(0, self.petCount):
                        print (self.nestAreaFrequency, self.modes)
                        #print(self.gapTime)
                        if abs(self.nestAreaFrequency[i]-self.modes[i][1]) > self.termTimer / 4:
                            #주석 분모 상수 여러 영상들로 테스트해서 조절 필요
                            self.wrongPetCount += 1
                    if self.wrongPetCount != 0:
                        if self.gapTime >= self.intervalTime:
                            self.msg = "%d"%self.wrongPetCount + '마리 펫의 움직임이 보이지 않습니다.'
                            print (self.msg)
                            self.mPush.insertMSG(item.user, self.msg) #PUSH wrongPetCount

                            self.previousTime = time.localtime()
                        self.wrongPetCount = 0


                #리스트 초기화
                self.petAreaCollection = []
                self.modes = []

            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def areaDetection(self, x, y):
        areaRow = 0
        areaCol = 0
        for i in range(0, self.col):
            if (i * self.width / self.col) < x and x < (i * self.width / self.col + self.width / self.col):
                areaCol = i
                break
        for i in range(0, self.row):
            if (i * self.height / self.row) < y and y < (i * self.height / self.row + self.height / self.row):
                areaRow = i
                break
        return areaRow, areaCol

    def optFlow(self, frame, prvs, hsv):

        next = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        k = cv2.waitKey(1) & 0xff

        prvs = next
        return prvs, hsv, bgr

    def getCenterOfContour(self, image):
        # load the image, convert it to grayscale, blur it slightly,
        # and threshold it

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpImage = cv2.filter2D(gray, -1, kernel)
        thresh = cv2.threshold(sharpImage, 60, 255, cv2.THRESH_BINARY)[1]

        # find contours in the thresholded image
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]

        # loop over the contours
        for c in cnts:
            if cv2.contourArea(c) > 0:
                # compute the center of the contour
                M = cv2.moments(c)
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                # draw the contour and center of the shape on the image
                cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
                cv2.circle(image, (cX, cY), 7, (255, 255, 255), -1)

                pointRow, pointCol = self.areaDetection(cX, cY)
                self.area[pointRow * self.col + pointCol] += 1

                for i in range(0, self.col):
                    cv2.line(image,
                             ( i * int(self.width / self.col), 0 ),
                             ( i * int(self.width / self.col), int(self.height - 1) ),
                             (0, 0, 255),
                             1)
                for i in range(0, self.row):
                    cv2.line(image,
                             ( 0, i * int(self.height / self.row) ),
                             ( int(self.width - 1), i * int(self.height / self.row) ),
                             (0, 0, 255),
                             1)

        self.maxIndex = 0

        for i in range(0, self.petCount):
            for j in range(1, self.row * self.col):
                if self.area[self.maxIndex] < self.area[j]:
                    self.maxIndex = j
            self.area[self.maxIndex] = 0
            self.petArea[i] = self.maxIndex

        self.petArea.sort()

        for i in range(0, self.petCount):
            self.petAreaCollection.append(self.petArea[i])


        cv2.imshow("Image", image)


    def capture(self):

        cv2.imwrite(self.imageDirectory + self.mPush.T.SERIAL + '.png', self.frame)

    def signalHandler(self, signum, frame):
        print('Signal generation!')
        self.cap.release()
        cv2.destroyAllWindows()
        sys.exit(0)

    def register_all_signal(self):
        ''' 모든 시그널 등록 '''
        for x in dir(signal):
            if not x.startswith("SIG"):
                continue

            try:
                signum = getattr(signal, x)
                signal.signal(signum, self.signalHandler)
            except:
                # signal 등록에 실패하는 경우 표시
                print('Skipping the signal : %s' % x)
                continue

    def modeFinder(self, list):  # list는 리스트나 튜플 형태의 데이터
        c = Counter(list)

        return c.most_common(self.row * self.col)

