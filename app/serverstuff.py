from flask import Flask, render_template, Response, request, session, redirect, url_for
from flask_socketio import SocketIO

# creating the flask application
app = Flask(__name__)
socketio = SocketIO(app)

# creating hashmaps to check the number of users in the room
users_in_room = {}
rooms_sid = {}
names_sid = {}

# storing a room's characteristics
@app.route("/join", methods=["GET"])
def join():
    display_name = request.args.get('display_name')
    # mute_audio = request.args.get('mute_audio') # 1 or 0
    mute_video = request.args.get('mute_video') # 1 or 0
    room_id = request.args.get('room_id')
    session[room_id] = {"name": display_name,"mute_video": mute_video} # "mute_audio": mute_audio

    return redirect(url_for("index"))
    # return redirect render_template("index.html", room_id=room_id, display_name=session[room_id]["name"], mute_video=session[room_id]["mute_video"])

    # mute_audio = session[room_id]["mute_audio"]

