import tornado.ioloop
import tornado.web
import tornado.websocket
import cv2
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

    def get_jpeg_image_bytes(self):
        ret, img = self.camera.read()
        return cv2.imencode('.jpg', img)[1].tobytes()


class ImageWebSocket(tornado.websocket.WebSocketHandler):
    clients = set()

    def check_origin(self, origin):
        # Allow access from every origin
        return True

    def open(self):
        ImageWebSocket.clients.add(self)
        logging.info("WebSocket opened from: " + self.request.remote_ip)

    def on_message(self, message):
        jpeg_bytes = camera.get_jpeg_image_bytes()
        self.write_message(jpeg_bytes, binary=True)

    def on_close(self):
        ImageWebSocket.clients.remove(self)
        logging.info("WebSocket closed from: " + self.request.remote_ip)


if __name__ == "__main__":
    script_path = os.path.dirname(os.path.realpath(__file__))
    static_path = script_path + '/static/'
    camera = Camera(args.camera)

    app = tornado.web.Application([
        (r"/websocket", ImageWebSocket),
        (r"/(.*)", tornado.web.StaticFileHandler, {'path': static_path, 'default_filename': 'index.html'}),
    ])
    app.listen(args.port)
    logging.info(f"Starting server: http://{args.host}:{args.port}")
    tornado.ioloop.IOLoop.current().start()