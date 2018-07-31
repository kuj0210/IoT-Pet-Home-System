#-*-coding: utf-8-*-
from flask import Flask,request,jsonify,send_from_directory, render_template
from flask_sslify import SSLify

from ChattingBot.file.sr_image import imageIO, initDir
from ChattingBot.file.cache import Cache
from ChattingBot.nl import usecase_finder
from ChattingBot.api.handler import Handler
from ChattingBot.auth.signup import *
from ChattingBot.ssl import config
from ChattingBot.device.pethome import Pethome

THusecaseFinder = usecase_finder.UsecaseFinder()
UPLOAD_FOLDER = 'uploaded'
initDir('uploaded')

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

    if postBodyMessage == "ECHO": return
    return jsonify(postBodyMessage), 200

@app.route("/bootUp",methods=["POST"])
def bootUpMobile():
    pethome = Pethome()
    return pethome.bootUp(request)

@app.route("/RQST",methods=["POST"])
def passRequest():
    pethome = Pethome()
    return pethome.sendRequest(request)
 
@app.route("/push",methods=["POST"])
def pushResult():
    pethome = Pethome()
    return pethome.push(request)

 
@app.route("/<user>/image",methods=["POST",'GET'])
def image(user):
    path = app.config['UPLOAD_FOLDER']
    return imageIO(request, user, Memo, path)

#파일전송
@app.route('/download/<filename>', methods=['GET'])
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename=filename)

#로그인
@app.route('/signup/<temp_user_key>', methods=['GET','POST'])
def sign_up(temp_user_key):
    regist = Register()
    if request.method == 'GET':
        return render_template('regist.html')

    else: # request.method == 'POST':
        user_key, is_registed = sigup(temp_user_key=temp_user_key, form=request.form)
        regist.insertUserRequest(user_key, "UPDATE")
        if is_registed:
            #msg = payload.getPostPushMessage(user=user_key, text=util.SUCESS_TO_REGIST)
            #sender.sendPush(url=util.PUSH_URL, user=user_key, msg=msg)
            return render_template("regist_success.html"), 200
        else:
            #msg = payload.getPostPushMessage(user=user_key, text=util.FAIL_TO_REGIST_USER)
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
    contextSSL = (config.cert, config.key)
    app.run(host='0.0.0.0', port=443, debug = True, ssl_context = contextSSL)
