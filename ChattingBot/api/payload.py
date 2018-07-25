def getImageBox(user, url):
    return {
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

def getUpdateBox(url):
    return {"imageUrl": url}

def getPostBodyMessage(user, text):
    return {
        "event": "send",
        "user": user,
        "textContent": {
            "text": text
        },
        "options": {
            "notification": "true"
        }
    }

def getPostPushMessage(user, text):
    return {
        "event": "send",
        "user": user,
        "textContent": {
            "text": text
        }
    }

def ImageJson(user, URL):
    return {
        "event": "send",
        "user": user,
        "imageUrl": URL
    }
