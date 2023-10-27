from app import app

@app.route('/')
def index():
    return 'Welcome to the chat application'

@app.route('/chat')
def chat():
    return 'Chat page'

@app.route('/user')
def user():
    return 'User page'
