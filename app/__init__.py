from flask import Flask
from flask_socketio import SocketIO
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app)

from app.routes import *
