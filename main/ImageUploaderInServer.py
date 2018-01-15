from flask import request, make_response
import threading

class ImageUploader(threading.Thread):
    def __init__(self):
        self.respnose = make_response()

    def run(self):
        print("EXECUTE UPLOAD OPERATION")
        try:
            image = request.files['image']
            image.save(image.filename)
            self.response.status_code = 204
        except Exception as e:
            print(e)
            self.response.status_code = 415

        return self.response