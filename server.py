from flask import Flask, request, jsonify
from flask_sockets import Sockets
from audio_rms import rms, ding
from df_detect import detect_intent_audio
import time
import os
import uuid

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_credentials.json"

Threshold = 10
CHANNELS = 1
TIMEOUT_LENGTH = 0.5 #The silent length we allow before cutting recognition
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
    rec = []
    current = 1
    end = 0

    while not ws.closed:
        
        audio = ws.receive()
        if isinstance(audio, str):
            continue #if this is a string, we don't handle it
        rms_val = rms(audio)


        #If audio is loud enough, set the current timeout to now and end timeout to now + TIMEOUT_LENGHT
        #This will start the next part that stores the audio until it's quiet again
        if rms_val > Threshold and not current <= end :
            print("Heard Something")
            current = time.time()
            end = time.time() + TIMEOUT_LENGTH

        #If levels are higher than threshold add audio to record array and move the end timeout to now + TIMEOUT_LENGTH
        #When the levels go lower than threshold, continue recording until timeout. 
        #By doing this, we only capture relevant audio and not continously call our STT/NLP with nonsensical sounds
        #By adding a trailing TIMEOUT_LENGTH we can capture natural pauses and make things not sound robotic
        if current <= end: 
            if rms_val >= Threshold: end = time.time() + TIMEOUT_LENGTH
            current = time.time()
            rec.append(audio)

        #process audio if we have an array of non-silent audio
        else:
            if len(rec)>0: 
                print("Audio Processing")

                output_audio = bytearray(ding()) #get our ding binary

                #When Devs can't name variables
                i = 0 
                
                #send Ding
                #Chunk out the output audio in 640 bytes and send to socket
                while (i <= len(output_audio)):
                    chunk = output_audio[i:i+640]
                    ws.send(chunk)
                    i +=640 

                #we join the bytearray into one big binary audio
                audio_to_process = b''.join(rec)
                #send it to Dialog flow (or any STT + NLP Combo you want. Using DF here since it'll handle STT and NLP)
                response = detect_intent_audio("move-test-xpjn", session_id, "en-US", audio_to_process)

                #make DF output audio into a byte array so we can chunk it easily 
                output_audio = bytearray(response.output_audio) 

                #again, When Devs can't name variables
                i = 0 
                
                #Chunk out the output audio in 640 bytes and send to socket
                while (i <= len(output_audio)):
                    chunk = output_audio[i:i+640]
                    ws.send(chunk)
                    i +=640 
                rec = [] #reset audio array to blank

                #Make our code do something about the intent
                intent_handler(response)

                #If intent is bye, end call
                if response.query_result.intent.display_name == "bye":
                    #wait 1 second so the audio can playback completely before cutting off
                    time.sleep(1)
                    ws.close()


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    
    server = pywsgi.WSGIServer(("", 8080), app, handler_class=WebSocketHandler)
    server.serve_forever()
