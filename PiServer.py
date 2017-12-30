from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/feed",methods=["POST"])
def setFeed():
    message = {
        "message" : {
            "text" : "펫에게 먹이를 주고 있어요."
        }
    }
    return jsonify(message), 200

@app.route("/water", methods=["POST"])
def setWater():
    message = {
        "message" : {
            "text" : "펫에게 물을 주고 있어요."
        }
    }
    return jsonify(message), 200


@app.route("/door", methods=["POST"])
def setDoor():
    message = {
        "message" : {
            "text" : "펫 하우스를 개방합니다."
        }
    }
    return jsonify(message), 200


@app.route("/camera", methods=["POST"])
def captureCamera():
    message = {
        "message" : {
            "text" : "사진을 찍었어요."
        }
    }
    return jsonify(message), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888, debug = True)
    
