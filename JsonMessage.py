from compare import UsecaseList
#
# This module uses to Server module for managing json data.
# Specially, This module manage json data that use to send or recieve kakao server.
# ** Json data usually use HTTP Protocol's body part.
#
usecase = UsecaseList()
usecase.setUsecae("water", ["마실", "음료", "물"], ["배식", "급여", "주다", "먹"], 50)
usecase.setUsecae("feed", ["밥", "먹", "사료", "간식", "식사"], ["배식", "급여", "주다", "먹"], 50)
usecase.setUsecae("open", ["문", "입구"], ["열", "오픈", "개방"], 100)
usecase.setUsecae("camera", ["사진", "상황", "모습", "얼굴", "현황"], ["보", "알", "보내"], 60)



class MessageClass :
    # This member function initialize kakao's keyboard setting.
    def getBaseKeyboard(self):
        baseKeyboard = {
            "type": "text"
        }
        # ** Currently, This part don't need to touch.
        return baseKeyboard

    # This member function send manager's message to user.
    # Also, It hava 3 ways of sending message(;feed,water,door).
    def postTextMessage(self, message):
        ##########################################################################
        # This part need to parsing message.
        # String 'message' will parse to "Noun, verbe, object".
        # And this components will make String 'result'.
        # String;result is important component to devide int 'if - else' sentence.

        result = usecase.analyzeSentence(message)

        ##########################################################################
        print(result)
        # Don't support command.

        sendMSG = '현재 지원되지 않는 기능이예요...'
        if 'feed'in result:
            sendMSG = "펫에게 먹이를 주고 있어요.\n"

            ##   Part1   ########################################################
            # Need to control RaspberryPi Sensor.                               #
            # This part need source code/module to control motor sensor.        #
            #####################################################################

        if 'water'in result:
            sendMSG += "펫에게 물을 주고 있어요.\n"

            ##   Part2   ########################################################
            # Need to control RaspberryPi Sensor.                               #
            # This part need source code/module to control motor sensor.        #
            #####################################################################

        if 'open'in result:
            sendMSG += "펫 하우스를 개방합니다.\n"

            ##   Part3   ########################################################
            # Need to control RaspberryPi Sensor.                               #
            # This part need source code/module to control motor sensor.        #
            #####################################################################



        ## This sentence is composed multimedia data;Photo.
        ## Therefore, this part only have return sentence.
        if 'camera'in result:
            ##   Part4   ########################################################
            # Need to control PiCamera module.                                  #
            #####################################################################
            cameraMessage = {
                'message': {
                    'text': '사진을 찍었어요!',
                    'photo': '/photo/pet.png',
                    'width': 640,
                    'height': 480
                },
                'keyboard': {
                    'type': 'text'
                }
            }
            return cameraMessage



        # Parsing and reunit message return to Server module.
        postBodyMessage = {
                'message': {
                    'text': sendMSG
                },
                'keyboard': {
                    'type': 'text'
                }
            }
        return postBodyMessage


