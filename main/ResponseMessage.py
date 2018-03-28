'''
Copyright (c) IoT-Pet-Home-system team : Woo-jin Kim, Keon-hee Lee, Dae-seok Ko
LICENSE : GPL v3 LICENSE

- Description : https://github.com/kuj0210/IoT-Pet-Home-System
- If you want to contact us, please send mail "beta1360@naver.com"
'''
import time

class Message :
    '''
    This class manage the messages for using response (Main-Server -> messenger API server).
    Therefore, this class call and make message to send user. 
    '''
    def __init__(self):
        self.PATH = "upload/"
        self.SERVER_URL = "https://pethome.ga:443/download/"

        self.MISTYPE_MESSAGE = "등록양식이 잘못되었습니다 :("
        self.REGISTED_USER = "이미 등록된 유저입니다 :("
        self.UNREGISTED_KEY = "등록되지 않은 키입니다. 기기 고유키를 다시 확인해주세요."
        self.SUCCESS_TO_REGIST = "등록이 완료되었습니다!"

        self.HOW_TO_USE = """아래의 사용설명서를 참고해주세요.\n
        https://github.com/kuj0210/opensourceproject"""

        self.successCameraMessage = "사진을 찍었어요!\n"

        # Fail Dict
        self.failWaterMessage = "펫에게 정상적으로 물을 주지 못했어요. 사용중이거나 작동하지 않습니다."
        self.failFeedMessage = "펫에게 정상적으로 먹이를 주지 못했어요. 사용중이거나 작동하지 않습니다."
        self.failDoorMessage = "펫 하우스를 정상적으로 열어주지 못했어요. 사용중이거나 작동하지 않습니다."
        self.failCameraMessage = "사진을 정상적으로 찍지 못했어요.. 카메라를 사용중이거나 작동하지 않습니다.."

        # Continue Dict
        self.continueWaterMessage = "펫에게 물을 주는 중이예요."
        self.continueFeedMessage = "펫에게 먹이를 주는 중이예요."
        self.continueDoorMessage = "펫 하우스를 열어주는 중이예요."
        self.continueCameraMessage = "사진을 찍고있어요."

    def regist_userMessage(self, message, user_key, mServerUtility):
        '''
        1. Arguement
            - message : data recieved from user
            - user_key : user information for searching database and using to query sentence.
            - mServerUtility : object to use this part.

        2. Output
            Result message : a message related "success or fail"

        3. Description
            This function make a message related "Is registration success or fail?" to user.
            If you send a correct type message("[등록]/email/PiKey"), you can recieve result message. 
        '''
        sendMSG = "None"

        try:
            data = message.split("/")
            email = data[1]
            PiKey = data[2]

        except:
            return self.MISTYPE_MESSAGE

        mServerUtility.openDB()
        regist_result = mServerUtility.getDatabase()\
            .insertUserData(platform="kakao-talk", user_key=user_key, email=email, PiKey=PiKey)
        mServerUtility.closeDB()

        if regist_result == "등록된 유저":
            sendMSG = self.REGISTED_USER

        elif regist_result == "등록되지 않은 키":
            sendMSG = self.UNREGISTED_KEY

        else:  # regist_result == "등록 완료"
            sendMSG = self.SUCCESS_TO_REGIST

        return sendMSG

    def inform_userInformation_Message(self, user_key, mServerUtility):
        '''
        1. Arguement
            - user_key : user information for searching database and using to query sentence.
            - mServerUtility : object to use this part.

        2. Output
            Result message : the email related user_key

        3. Description
            This function make a message related to inform your email.
        '''
        mServerUtility.openDB()
        sendMSG = mServerUtility.getDatabase().findUserEmail(platform="kakao-talk", user_key=user_key)
        mServerUtility.openDB()

        return sendMSG

    def inform_howToUse_Message(self):
    #Description : Getter function related howToUse
        return self.HOW_TO_USE

    def operation_result_Message(self, getResultByPiServer, ServerUtility, user_key):
        '''
        1. Arguement
            - getResultByPiServer : json type message, executing result, from pi-server
            - ServerUtility : the object to use this part.
            - user_key : user information for searching database and using to query sentence.

        2. Output
            Result message : response message to send the user.

        3. Description
            This function make a message related to inform operation result. In other words, this func transform
            json type message to plain-text type message. This plain-text feel communication to chat-bot.

            If you use a kakao-platform chatting and request camera operation, you recieve imagefile path.
            Because kakao-platform API server don't support to send a sufficient size of image.
        '''
        sendMSG = "None"

        if getResultByPiServer["water"] == "use":
            if sendMSG == "None":
                sendMSG = self.continueWaterMessage
            else:
                sendMSG += "\n" + self.continueWaterMessage
        elif getResultByPiServer["water"] == "using":
            if sendMSG == "None":
                sendMSG = self.failWaterMessage
            else:
                sendMSG += "\n" + self.failWaterMessage

        if getResultByPiServer["feed"] == "use":
            if sendMSG == "None":
                sendMSG = self.continueFeedMessage
            else:
                sendMSG += "\n" + self.continueFeedMessage
        elif getResultByPiServer["feed"] == "using":
            if sendMSG == "None":
                sendMSG = self.failFeedMessage
            else:
                sendMSG += "\n" + self.failFeedMessage

        if getResultByPiServer["door"] == "use":
            if sendMSG == "None":
                sendMSG = self.continueDoorMessage
            else:
                sendMSG += "\n" + self.continueDoorMessage
        elif getResultByPiServer["door"] == "using":
            if sendMSG == "None":
                sendMSG = self.failDoorMessage
            else:
                sendMSG += "\n" + self.failDoorMessage

        if getResultByPiServer["camera"] == "use":
            ServerUtility.openDB()
            print("이미지 파일 받는중...")
            response = ServerUtility \
                .getImageFileFromPiServer(platform="kakao-talk", user_key=user_key)
            ServerUtility.closeDB()

            now = time.localtime()
            IMAGENAME = "Screenshot_%04d-%02d-%02d_%02d-%02d-%02d.png" \
                        % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

            ServerUtility.imageReciever(response=response, filename=self.PATH + IMAGENAME)

            print("image making success. %s" % (self.PATH + IMAGENAME))
            if sendMSG == "None":
                sendMSG = self.successCameraMessage
                sendMSG += self.SERVER_URL + self.PATH + IMAGENAME
            else:
                sendMSG += self.successCameraMessage
                sendMSG += self.SERVER_URL + self.PATH + IMAGENAME

        elif getResultByPiServer["camera"] == "using":
            if sendMSG == "None":
                sendMSG = self.failCameraMessage
            else:
                sendMSG += "\n" + self.failCameraMessage

        return sendMSG
