#from flask import Flask, render_template
#from flask_socketio import SocketIO, send, emit
import socketio
import base64
import eventlet
eventlet.monkey_patch()
import logging
import threading
import time
from json import dumps

sio = socketio.Server(cors_allowed_origins='*', async_mode='eventlet')
app = socketio.WSGIApp(sio)

def data_to_json(data):
    data = {
        'data': data
    }
    json = dumps(data, ensure_ascii=False, default=str).encode('utf-8')
    return json


def update_dashboard_info(data):
    print('[SOCKET] Sending info')
    json = data_to_json(data)
    sio.emit('dashboard', json)

def send_plate_picture(picture):
    print('[SOCKET] Sending picture')
    json = data_to_json(picture)
    #socketio.send('license_plate', json)
    sio.emit('license_plate', json)

@sio.event
def debug(sid, environ):
    print('[SOCKET] debug ')

@sio.event
def connect(sid, environ):
    print('[SOCKET] Client connected')

@sio.event
def disconnect(sid, environ):
    print('[SOCKET] Client disconnected')


def serve():
    print("[SOCKET] Starting")
    sock = eventlet.listen(('', 5000))
    eventlet.wsgi.server(sock, app, debug=True)
    #app.run(host='0.0.0.0', port=5001)
    #socketio.run(app, host='0.0.0.0', cors_allowed_origins='*')
    #socketio.run(app)
    print("[SOCKET] Stopped")


x = threading.Thread(target=serve)
x.start()
