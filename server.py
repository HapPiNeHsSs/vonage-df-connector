from flask import Flask, request, jsonify
from flask_sockets import Sockets

from df_detect import detect_intent_audio, process_audio
import time
import os
import uuid



CHANNELS = 1
CHUNK_SIZE = 640 #Required Chunk Size by Vonage for 1600
PACKAGE_TIMEOUT = 4
package = ''
package_expire = 0
session_id = ""

def intent_handler(response):
    global package
    global package_expire
    package = response.query_result.intent.display_name
    package_expire = time.time() + PACKAGE_TIMEOUT
    return "Package set to "+package
    #this will handle the intents and make our app do something about it

#initiate our flask app
app = Flask(__name__)
sockets = Sockets(app)

@app.route("/set_package")
def set_package():
    global package
    global package_expire
    package = request.args.get('package')
    package_expire = time.time() + PACKAGE_TIMEOUT
    return "Package set to "+package
    
@app.route("/get_package")
def get_package():
    global package
    current = time.time()
    if current >= package_expire:
        package = ''
        return ''
    p = package
    package = ''
    return p

@app.route("/ncco")
def answer_call():
    print("ncc0")

    #set a new session ID each call. This will ensure that Dialogflow convos are refreshed
    global session_id
    session_id = str(uuid.uuid4())
    ncco = [
        {
            "action": "talk",
            "text": "DF connector",
        },
        {
            "action": "connect",
            "from": "NexmoTest",
            "endpoint": [
                {
                    "type": "websocket",
                    "uri": "ws://vonage.urzo.online/socket".format(request.host),
                    "content-type": "audio/l16;rate=16000",
                }
            ],
        },
    ]
    print("ws://vonage.urzo.online/socket".format(request.host))
    return jsonify(ncco)


@app.route("/webhooks/event", methods=["POST"])
def events():
    return "200"

@sockets.route("/socket", methods=["GET"])
def echo_socket(ws):
    process_audio(ws, session_id, intent_handler)


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    
    server = pywsgi.WSGIServer(("", 8080), app, handler_class=WebSocketHandler)
    server.serve_forever()
