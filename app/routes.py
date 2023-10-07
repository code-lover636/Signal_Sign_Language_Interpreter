import pickle
import struct

from flask import Flask, render_template, Response
from flask_socketio import SocketIO

from app import app

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

@SocketIO.on('connect')
def handle_connect():
    print('Client connected')

@SocketIO.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@SocketIO.on('request_frame')
def send_frame():
    for frame in generate_frames():
        socketio.emit('frame', frame)

@Socketio.on('message')
def handle_message(data):
    print('Received message:', data)
    # Broadcast the message to all connected clients
    socketio.emit('message', data)

# Add more custom events as needed

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=9999, allow_unsafe_werkzeug=True)

