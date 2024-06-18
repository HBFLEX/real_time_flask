from flask import Flask, render_template
from flask_socketio import SocketIO, send
import secrets


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)

socketIO = SocketIO(app)

@app.route('/')
def home_page():
    return render_template('index.html')


@socketIO.on('message')
def handleMessage(msg):
    print(f'Message: {msg}')
    send(msg, broadcast=True)

@socketIO.on('connect')
def connect():
    print('connected')

if __name__ == '__main__':
    socketIO.run(app, debug=True)

