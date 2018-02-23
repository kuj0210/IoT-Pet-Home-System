class Message :
    successCameraMessage = "사진을 찍었어요!\n"

    def getSuccessCameraMessage(self):
        return self.successCameraMessage

    #Fail Dict
    failWaterMessage = "펫에게 정상적으로 물을 주지 못했어요. 사용중이거나 작동하지 않습니다."
    failFeedMessage = "펫에게 정상적으로 먹이를 주지 못했어요. 사용중이거나 작동하지 않습니다."
    failDoorMessage = "펫 하우스를 정상적으로 열어주지 못했어요. 사용중이거나 작동하지 않습니다."
    failCameraMessage = "사진을 정상적으로 찍지 못했어요.. 카메라를 사용중이거나 작동하지 않습니다.."

    def getFailWaterMessage(self):
        return self.failWaterMessage

    def getFailFeedMessage(self):
        return self.failFeedMessage

    def getFailDoorMessage(self):
        return self.failDoorMessage

    def getFailCameraMessage(self):
        return self.failCameraMessage

    #Continue Dict
    continueWaterMessage = "펫에게 물을 주는 중이예요."
    continueFeedMessage = "펫에게 먹이를 주는 중이예요."
    continueDoorMessage = "펫 하우스를 열어주는 중이예요."
    continueCameraMessage = "사진을 찍고있어요."

    def getContinueWaterMessage(self):
        return self.continueWaterMessage

    def getContinueFeedMessage(self):
        return self.continueFeedMessage

    def getContinueDoorMessage(self):
        return self.continueDoorMessage

    def getContinueCameraMessage(self):
        return self.continueCameraMessage
