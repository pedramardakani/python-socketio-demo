import socketio

SIO_MODE: str = "asgi"

# Socket setup
sio = socketio.AsyncServer(async_mode=SIO_MODE, cors_allowed_origins='*')

# Need to call this in FastAPI
socket_app = socketio.ASGIApp(socketio_server=sio)

# Basic events
@sio.event
async def connect(sid, env):
    print(f"on connect: {sid}")

@sio.event
async def disconnect(sid):
    print(f"on disconnect: {sid}")

@sio.event
async def echo(sid, data):
    # Print on server console
    print(f"Received: sid <{sid}>\ndata: '{data}'")

    # Return an acknowledgment message for client
    return f"Server heard you say: '{data}'"

def create_app():
    return socket_app
