from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

active_rooms = set()  # To keep track of active rooms

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    active_rooms.add(room)  # Store the room as an active room
    emit('joined', {'room': room}, room=room)

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)
    active_rooms.remove(room)  # Remove the room from the list of active rooms
    emit('left', {'room': room}, room=room)

@socketio.on('message')
def handle_message(data):
    room = data['room']
    message = data['message']
    emit('message', {'message': message}, room=room)

@socketio.on('disconnect')
def handle_disconnect():
    for room in active_rooms:
        leave_room(room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
