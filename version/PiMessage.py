class PiMessage :
    #Success Dictcontinue
    successWaterMessage = {"message" : {"text" : "펫에게 물을 줬어요!" } }
    successFeedMessage = {"message" : {"text" : "펫에게 먹이를 줬어요!" } }
    successDoorMessage = {"message" : {"text" : "펫 하우스를 열어줬어요!"} }
    successCameraMessage = {"message": {"text": "사진을 찍었어요."} }

    def getSuccessWaterMessage(self):
        return self.successWaterMessage

    def getSuccessFeedMessage(self):
        return self.successFeedMessage

    def getSuccessDoorMessage(self):
        return self.successDoorMessage

    def getSuccessCameraMessage(self):
        return self.successCameraMessage

    #Fail Dict
    failWaterMessage = {"message" : {"text" : "펫에게 정상적으로 물을 주지 못했어요. 센서 확인 부탁드릴게요." } }
    failFeedMessage = {"message" : {"text" : "펫에게 정상적으로 먹이를 주지 못했어요. 센서 확인 부탁드릴게요." } }
    failDoorMessage = {"message" : {"text" : "펫 하우스를 정상적으로 열어주지 못했어요. 확인 부탁해용 ㅠㅠ"} }
    failCameraMessage = {"message": {"text": "사진을 정상적으로 찍지 못했어요..."} }

    def getFailWaterMessage(self):
        return self.failWaterMessage

    def getFailFeedMessage(self):
        return self.failFeedMessage

    def getFailDoorMessage(self):
        return self.failDoorMessage

    def getFailCameraMessage(self):
        return self.failCameraMessage

    #Continue Dict
    continueWaterMessage = {"message" : {"text" : "펫에게 물을 주는 중이예요. 잠시 후 시도해주세요!" } }
    continueFeedMessage = {"message" : {"text" : "펫에게 먹이를 주는 중이예요.  잠시 후 시도해주세요!" } }
    continueDoorMessage = {"message" : {"text" : "펫 하우스를 열어주는 중이예요. 잠시 후 시도해주세요!"} }
    continueCameraMessage = {"message": {"text": "사진을 찍고있어요. 잠시 후 시도해주세요!"} }

    def getContinueWaterMessage(self):
        return self.continueWaterMessage

    def getContinueFeedMessage(self):
        return self.continueFeedMessage

    def getContinueDoorMessage(self):
        return self.continueDoorMessage

    def getContinueCameraMessage(self):
        return self.continueCameraMessage