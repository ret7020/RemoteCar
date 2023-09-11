import tornado.ioloop
import tornado.web
import tornado.websocket
import cv2
from PIL import Image
import argparse
import logging
import os

logging.basicConfig(level=logging.INFO)
parser = argparse.ArgumentParser(description='Run Software on SBC')
parser.add_argument('--port', default=8888, type=int, help='Web server port (default: 8888)')
parser.add_argument('--host', default="0.0.0.0", type=str, help='Web server host (default: 0.0.0.0 - listen for all)')
parser.add_argument('--camera', default=0, type=int, help='Camera index to read from (default: 0)')
args = parser.parse_args()

class Camera:
    def __init__(self, index) -> None:
        self.camera = cv2.VideoCapture(index)
        logging.info("Camera inited")


if __name__ == "__main__":
    script_path = os.path.dirname(os.path.realpath(__file__))
    static_path = script_path + '/static/'
    camera = Camera(args.camera)