from flask import Flask
from flask_socketio import SocketIO
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)  # WSGI
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY
socketio = SocketIO(app)
db = SQLAlchemy(app)
Config.validate_database()
bcrypt = Bcrypt()  # Create a Bcrypt instance

from app.routes import *
