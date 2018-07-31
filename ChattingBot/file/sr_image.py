import os
from datetime import datetime

from . import cache
from ChattingBot.api import sender, util

def initDir(path):
    try:
        if not os.path.isdir(path):
            os.mkdir(path)
        return True

    except:
        return False

def imageIO(request, user, memo, path):
    file =request.files['file'] #파일받기
    filename=file.filename # 이름얻기
    serial=filename.split(".")[0] #시리얼번호 추출
    now = datetime.now()# 시간얻기
    f =filename.split(".") #파싱
    sndF =f[0] +'_%s-%s-%s-%s-%s-%s.' % ( now.year, now.month, now.day,now.hour,now.minute,now.second )+f[1]
    # 파일이름 완성

    # 이전에 저장한것 삭제
    res = memo.dememorization(f[0])
    if res !=False:
        os.remove(res)
    #파일저장
    file.save(os.path.join(path,sndF))
    sender.sendIMAG(user,util.IMAGE_URL +sndF)

    #방금 저장한 파일 기억
    memo.memorization(f[0],os.path.join(path,sndF))
    return "TRUE"