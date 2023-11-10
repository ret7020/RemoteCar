from flask import Flask, render_template
from flask_sock import Sock
import logging
import cv2
import numpy as np
# import threading
import time
import sys
import gzip
import base64

class Camera:
    def __init__(self, index) -> None:
        self.camera = cv2.VideoCapture(index)
        self.encode_params = [int(cv2.IMWRITE_JPEG_QUALITY), 70]
        self.image = cv2.imencode('.jpg', np.zeros((480, 640)), self.encode_params)[1].tobytes()
        logging.info("Camera inited")

    def get_jpeg_image_bytes(self):
        ret, img = self.camera.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        res = cv2.imencode('.jpg', img, self.encode_params)[1].tobytes()
        #res = gzip.compress(res)
        return res

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

sock = Sock(app)
camera = Camera(0)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/control', methods=['POST'])
def api_manual_control():
    pass


@sock.route('/image')
def stream(sock):
    logging.error("Stream started")
    while True:
        sock.send(camera.get_jpeg_image_bytes())
        
