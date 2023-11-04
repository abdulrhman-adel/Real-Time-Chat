from app import app, socketio
from app.config import Config


if __name__ == '__main__':
    socketio.run(app, debug=True)
