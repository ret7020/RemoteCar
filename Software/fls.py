from flask import Flask, render_template
from flask_sock import Sock
import time
import logging
import cv2


class Camera:
    def __init__(self, index) -> None:
        self.camera = cv2.VideoCapture(index)
        logging.info("Camera inited")

    def get_jpeg_image_bytes(self):
        ret, img = self.camera.read()
        return cv2.imencode('.jpg', img)[1].tobytes()


app = Flask(__name__)
sock = Sock(app)
camera = Camera(0)

@app.route('/')
def index():
    return render_template('index.html')


@sock.route('/image')
def echo(sock):
    while True:
        sock.send(camera.get_jpeg_image_bytes())
        # time.sleep(0.0)