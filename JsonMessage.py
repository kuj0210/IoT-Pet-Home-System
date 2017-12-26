#
# This module uses to Server module for managing json data.
# Specially, This module manage json data that use to send or recieve kakao server.
# ** Json data usually use HTTP Protocol's body part.
#

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

        result = message

        ##########################################################################

        if result == 'feed':
            sendMSG = '우리 애완용에게 먹이를 주고 있어요.'

            ##   Part1   ########################################################
            # Need to control RaspberryPi Sensor.                               #
            # This part need source code/module to control motor sensor.        #
            #####################################################################

        elif result == 'water':
            sendMSG = '우리 애완용에게 물을 주고 있어요.'

            ##   Part2   ########################################################
            # Need to control RaspberryPi Sensor.                               #
            # This part need source code/module to control motor sensor.        #
            #####################################################################

        elif result == 'door':
            sendMSG = '우리 애완용 집 문을 열어줍니다 :)'

            ##   Part3   ########################################################
            # Need to control RaspberryPi Sensor.                               #
            # This part need source code/module to control motor sensor.        #
            #####################################################################

        ## This sentence is composed multimedia data;Photo.
        ## Therefore, this part only have return sentence.
        elif result == 'camera':
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

        # Don't support command.
        else :
            sendMSG = '현재 지원되지 않는 기능이예요...'

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



