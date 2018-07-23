#-*-coding: utf-8-*-
import os
from datetime import datetime

from flask import Flask,request,jsonify,send_from_directory, render_template
from flask_sslify import SSLify

from db.Register import *
from memo.cache import Cache
from nl import usecase_finder
from api.handler import Handler
from api import sender, util, payload
from auth.signup import *

THusecaseFinder = usecase_finder.UsecaseFinder()
UPLOAD_FOLDER = 'uploaded'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
sslfy =SSLify(app, permanent=True)
Memo = Cache()

@app.route("/",methods=["POST"])
def naver_Servermain():
   
    # make manager
    Manager = Handler()
    # get data from naver  talk talk
    dataFromMessenger =request.get_json()# get json data from naver talk talk
    infomationFromNaverTalk=Manager.getDataFromNaverTalk(dataFromMessenger) # it is process for data sorting
    postBodyMessage = Manager.eventHandler(infomationFromNaverTalk) # process event

    if postBodyMessage == "ECHO":
      return
    return jsonify(postBodyMessage), 200

@app.route("/bootUp",methods=["POST"])
def bootUpMobile():
    # make manager
    reg = Register()
    dataFromMessenger =request.get_json()# get json data from naver talk talk
    SR=dataFromMessenger['textContent']['text']

    UK=reg.getUserFromSerial(SR)
    print(UK)
    PCNT = reg.getPetCountFromSerial(SR)
    UK=str(PCNT)+'\n'+UK
    #UK.insert(0, PCNT)
    return UK 

@app.route("/RQST",methods=["POST"])
def passRequest():
    reg = Register()
    dataFromMessenger =request.get_json()# ge/home/test"t json data from naver talk talk
    SR=dataFromMessenger['textContent']['text']
    rq=reg.fetchRequest(SR)
    if rq == False:
        return "NO"
    return rq
 
@app.route("/push",methods=["POST"])
def pushResult():
    nM=Handler()
    dataFromMessenger =request.get_json()# get json data from naver talk talk
    user =msg=dataFromMessenger['user']
    msg=dataFromMessenger['textContent']['text']
    #DB에서 펫홈이름 얻기
    # 펫홈이름에서 알려드립니다 + msg를 아래의 푸쉬함수에 넣음
    sender.sendPush(util.PUSH_URL,user,msg)
    return "True"

 
@app.route("/<user>/image",methods=["POST",'GET'])
def image(user):
    nM=Handler()
    file =request.files['file'] #파일받기
    filename=file.filename # 이름얻기
    SR=filename.split(".")[0] #시리얼번호 추출
    now = datetime.now()# 시간얻기
    f =filename.split(".") #파싱
    sndF =f[0] +'_%s-%s-%s-%s-%s-%s.' % ( now.year, now.month, now.day,now.hour,now.minute,now.second )+f[1]
    # 파일이름 완성

    # 이전에 저장한것 삭제
    res = Memo.dememorization(f[0])
    if res !=False:
        os.remove(res)
    #파일저장
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],sndF))
    sender.sendIMAG(user,util.IMAGE_URL +sndF)

    #방금 저장한 파일 기억
    Memo.memorization(f[0],os.path.join(app.config['UPLOAD_FOLDER'],sndF))
    return "TRUE"

#파일전송
@app.route('/download/<filename>', methods=['GET'])
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename)

#로그인
@app.route('/signup/<temp_user_key>', methods=['GET','POST'])
def sign_up(temp_user_key):
    if request.method == 'GET':
        return render_template('regist.html')

    else: # request.method == 'POST':
        user_key, is_registed = sigup(temp_user_key=temp_user_key, form=request.form)
        if is_registed:
            msg = payload.getPostPushMessage(user=user_key, text=util.SUCESS_TO_REGIST)
            #sender.sendPush(url=util.PUSH_URL, user=user_key, msg=msg)
            return render_template("regist_success.html"), 200
        else:
            msg = payload.getPostPushMessage(user=user_key, text=util.FAIL_TO_REGIST_USER)
            #sender.sendPush(url=util.PUSH_URL, user=user_key, msg=msg)
            return render_template("regist_fail.html"), 200

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return render_template("error404.html"), 404

@app.errorhandler(405)
def not_allow_method(error):
    app.logger.error(error)
    return render_template("error405.html"), 405

if __name__ == "__main__":
    ## www 키
    #ssl_cert = '/etc/letsencrypt/live/www.kit-iot-system.tk/fullchain.pem'
    #ssl_key =  '/etc/letsencrypt/live/www.kit-iot-system.tk/privkey.pem'
    #일반키
    ssl_cert = '/etc/letsencrypt/live/kit-iot-system.tk/fullchain.pem'
    ssl_key =  '/etc/letsencrypt/live/kit-iot-system.tk/privkey.pem'
    contextSSL =  (ssl_cert, ssl_key)
    #user ="u9-NF6yuZ8H8TAgj1uzqnQ"
    app.run(host='0.0.0.0', port=443, debug = True, ssl_context = contextSSL)
    
