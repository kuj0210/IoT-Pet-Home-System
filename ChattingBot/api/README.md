# api modules

This module handle NaverTalkTalk(Web application messenger used by this system) API payload.

## Module handler

### class Handler

This class parse payload that is sent by NaverTalkTalk API server. </br>
And on request, this class send reply data to NaverTalkTalk API server.</br>

```python
def eventHandler(self, infomationFromNaverTalk)
```
  - **input**: infomationFromNaverTalk(dictionary)
  - **output**: postBodyMessage(dictionary)
  - **Description**: According to infomationFromNaverTalk, the message available will vary. 
In each ```if - else```, sendMSG(string) will be made and then get dictionary from ```payload.getPostBodyMessage(user, sendMSG)```.
This dictionary should be analytical in NaverTalkTalk API server.

```python
def handlerForSendEvent(self,user,msg)
```
  - **input**: user(string), msg(string)
  - **output**: message(string)
  - **discription**: First, ```msg``` will be parsed by ```usecaseFinder.analyzeSentence(msg)```. 
  And then, ```requestlist``` be returned by commands or pet-home operation keywords. 
  If this ```requestlist``` is commands(```howToUse``` or ```regist```), this method will return reply according commands. 
  If not commands(pet-home operation keywords), this method insert this keyword to database using ```self.regist.insertUserRequest(user," ".join(requestlist))```.
  And then, it return reply message according result.
  
```python
def getDataFromNaverTalk(self, dataFromMessenger)
```
  - **input**: dataFromMessenger(dictionary)
  - **output**: dicForSaveUserData(dictionary)
  - **discription**: NaverTalkTalk send data according [API document](https://github.com/navertalk/chatbot-api), but this data needs to be processed.
  This method examine dictionary key and values, and make it a suitable dictionary(```dicForSaveUserData```) for use in this class. In other words, 
  original data(```dataFromMessenger```) is changed to the data of user-key and message-oriented(```dicForSaveUserData```).


## Module payload

```python
def getImageBox(user, url)
```

  - **input**: user(string), url(string)
  - **output**: Message(using **image reply**) to use sending NaverTalkTalk API Server(dictionary)
                
```json
{
    "event": "send",
    "user": user,
    "compositeContent": {
        "compositeList": [{
            "title": "펫홈사진",
            "description": "요청하신 사진입니다",
            "image": {
                "imageUrl": url
            }
        }]
    }
}
```

```python
def getPostBodyMessage(user, text)
```

  - **input**: user(string), text(string)
  - **output**: Message(using **text reply**) to use sending NaverTalkTalk API Server(dictionary)
                
```json
{
    "event": "send",
    "user": user,
    "textContent": {
        "text": text
    },
    "options": {
        "notification": "true"
    }
}
```

```python
def getPostPushMessage(user, text)
```

  - **input**: user(string), text(string)
  - **output**: Message(using **push**) to use sending NaverTalkTalk API Server(dictionary)
  
```json
{    
    "event": "send",
    "user": user,
    "textContent": {
        "text": text
    }
}
```


## Module sender

```python
def sendPush(url, user, msg)
```
  
  - **input**: url(string), user(string), msg(string)
  - **discription**: This function make request to NaverTalkTalk API Server for sending **push message** to user. 
  Therefore ```user```(user_key) must be required, ``url`` is NaverTalkTalk API Server, ```msg``` is push message's text part.

```python
def sendIMAG(user, URL)
```
  
  - **input**: user(string), URL(string)
  - **discription**: This function make request to NaverTalkTalk API Server for sending **image message** to user.
   Therefore ```user```(user_key) must be required, ``URL`` is NaverTalkTalk API Server.


## Module util

 This module handle many data to relate to API utility. This module include NaverTalkTalk API server's url, this system's url,
 utility data and function. 
