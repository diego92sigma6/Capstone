from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import base64
import eventlet
import logging
import threading
import time
from json import dumps

# create a Socket.IO server
app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'

#original
socketio = SocketIO(app, cors_allowed_origins='*')

#eventlet experiment
#socketio = SocketIO(async_mode='eventlet')

def data_to_json(data):
    data = {
        'data': data
    }
    json = dumps(data, ensure_ascii=False, default=str).encode('utf-8')
    return json

def update_dashboard_info(data):
    print('[SOCKET] Sending info')
    json = data_to_json(data)
    socketio.send('dashboard', json)

def send_plate_picture(picture):
    print('[SOCKET] Sending picture')
    json = data_to_json(picture)
    socketio.send('license_plate', json)

@socketio.on('debug')
def debug():
    print('[SOCKET] debug ')

@socketio.on('connect')
def connect():
    print('[SOCKET] Client connected')

@socketio.on('disconnect')
def disconnect():
    print('[SOCKET] Client disconnected')

@socketio.on_error_default  
def default_error_handler(e):
    print('[SOCKET] Error: %s'%(e))


def serve():
    print("[SOCKET] Starting")
    #eventlet.wsgi.server(eventlet.listen(('', 5001)), app)
    #app.run(host='0.0.0.0', port=5001)
    #socketio.run(app, host='0.0.0.0', cors_allowed_origins='*')
    socketio.run(app)
    print("[SOCKET] Stopped")

x = threading.Thread(target=serve)
x.start()