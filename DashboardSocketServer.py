import socketio
import base64

# create a Socket.IO server
sio = socketio.Server()

# wrap with a WSGI application
app = socketio.WSGIApp(sio)

def update_dashboard_info(data):
    print('[SOCKET] Sending info')
    sio.emit('dashboard', {
        'data': data
    })

def send_plate_picture(picture):
    print('[SOCKET] Sending picture')
    b64 = base64.b64encode(picture)
    sio.emit('license_plate', {
        'data': b64
    })

@sio.event
def connect(sid, environment):
    print('[SOCKET] Client connected (',sid,')')

@sio.event
def disconnect(sid):
    print('[SOCKET] Client disconnected (',sid,')')

