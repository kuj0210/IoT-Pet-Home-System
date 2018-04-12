import numpy as np
import cv2
import time

cap = cv2.VideoCapture('test.mp4') #웹켐쓸거면인자 0 , 영상파일 열거면 이름 넣을것
fgbg = cv2.createBackgroundSubtractorMOG2()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


A = []
x = 1
y = 1

prevTime = time.time()


while (1):
    curTime = time.time()
    t = curTime - prevTime

    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    kernel = np.ones((3, 3), np.float32) / 25
    dst = cv2.filter2D(fgmask, -1, kernel)
    edges = cv2.Canny(dst, 100, 200)

    for i in range(0,width):
        for j in range(0,height):
            if edges[j,i] == 0:
                edges[j,i] = 255
            else :
                edges[j,i] = 0
                if t < 10:
                    A.append([j, i])


    if t < 10 :
        for i in range(len(A)):
            y = y + A[i][0]
            x = x + A[i][1]
        if len(A) != 0:
            x = x/len(A)
            y = y/len(A)

    if t>2:
        cv2.rectangle(edges, (int(x), int(y)), (int(x), int(y)), (0, 0, 255), 8)
        cv2.rectangle(frame, (int(x) - 130, int(y) - 170), (int(x) + 130, int(y) + 170), (0, 0, 255), 3)

    cv2.imshow('fgmask', frame)
    #cv2.imshow('frame', fgmask)
    #cv2.imshow('dst', dst)
    cv2.imshow('EDGES', edges)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


print(A)
cap.release()
cv2.destroyAllWindows()
