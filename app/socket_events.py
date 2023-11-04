from app import socketio
from flask_socketio import emit, send, join_room, leave_room, close_room, rooms, disconnect
from time import localtime, strftime

ROOMS = ['lounge', 'news', 'games', 'coding']


@socketio.on('message')
def handle_message(data):
    if isinstance(data, dict):
        user = data.get('user')
        msg = data.get('msg')
        room = data.get('room')
        time = strftime('%I:%M %p', localtime())
        if msg == '':
            return
        else:
            print(f"\n \n Message: {data} \n \n")
            print(f" Message: {msg}")
            print(f"User: {user}")
            print(f"Room: {room}")
            print(f" Time: {time} ")

            send({'msg': msg, 'user': user, 'time': time}, room=room)  # send to all clients
    else:
        return 'Invalid data'


@socketio.on('leave')
def handle_leave(data):
    if isinstance(data, dict):
        room = data.get('room')
        user = data.get('username')
        print("leave")
        leave_room(room)
        print(f"\n \n Message: {data} \n \n")
        print(f"User: {user}")
        print(f"Room: {room}")
        send({'msg': f"{user} has left the {room} room"}, room=room)
    else:
        return 'Invalid data'


@socketio.on('join')
def handle_join(data):
    if isinstance(data, dict):
        room = data.get('room')
        user = data.get('username')
        print("join")
        join_room(room)
        print(f"\n \n Message: {data} \n \n")
        print(f"User: {user}")
        print(f"Room: {room}")
        send({'msg': f"{user} has joined {room} room"}, room=room)
    else:
        return 'Invalid data'
