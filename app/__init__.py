from flask import Flask
from flask_socketio import SocketIO
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)  # WSGI
app.config.from_object(Config)
app.secret_key = Config.SECRET_KEY
socketio = SocketIO(app)
db = SQLAlchemy(app)
Config.validate_database()
bcrypt = Bcrypt()  # Create a Bcrypt instance
bcrypt.init_app(app)  # Initialize Bcrypt with the Flask app
login_manager = LoginManager()  # Create a LoginManager instance
login_manager.init_app(app)  # Initialize LoginManager with the Flask app

from app.routes import *
from app.socket_events import *
