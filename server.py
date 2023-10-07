import cv2
import pickle
import struct
from flask import Flask, render_template, Response
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')  # Create an HTML template for your interface

def generate_frames():
    vid = cv2.VideoCapture(0)
    while True:
        ret, image = vid.read()
        img_serialize = pickle.dumps(image)
        message = struct.pack("Q", len(img_serialize)) + img_serialize
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + message + b'\r\n')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('request_frame')
def send_frame():
    for frame in generate_frames():
        socketio.emit('frame', frame)

if __name__ == '__main__':
    app.debug = True  # Enable debugging
    socketio.run(app, host='0.0.0.0', port=9999, allow_unsafe_werkzeug=True)




