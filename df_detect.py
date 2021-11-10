from google.cloud import dialogflow
from audio_rms import rms, ding
import os, time

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_credentials.json"

SAMPLE_RATE = 16000
Threshold = 10
TIMEOUT_LENGTH = 0.5 #The silent length we allow before cutting recognition

def process_audio(ws, session_id, intent_handler):
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

#copied this from google, modified it a bit so it accepts binary data instead of audio file
def detect_intent_audio(project_id, session_id, language_code, input_audio):

    session_client = dialogflow.SessionsClient()

    audio_encoding = dialogflow.AudioEncoding.AUDIO_ENCODING_LINEAR_16

    session = session_client.session_path(project_id, session_id)

    audio_config = dialogflow.InputAudioConfig(
        audio_encoding=audio_encoding,
        language_code=language_code,
        sample_rate_hertz=SAMPLE_RATE,
    )
    speech_config = dialogflow.SynthesizeSpeechConfig(
            voice=dialogflow.VoiceSelectionParams(ssml_gender=dialogflow.SsmlVoiceGender.SSML_VOICE_GENDER_FEMALE))
    output_audio_config = dialogflow.OutputAudioConfig(
            audio_encoding=audio_encoding,
            sample_rate_hertz=SAMPLE_RATE,
            synthesize_speech_config=speech_config)

    query_input = dialogflow.QueryInput(audio_config=audio_config)

    request = dialogflow.DetectIntentRequest(
        session=session, query_input=query_input, input_audio=input_audio, output_audio_config=output_audio_config
    )
    response = session_client.detect_intent(request=request)

    print("=" * 20)
    print("Query text: {}".format(response.query_result.query_text))
    print(
        "Detected intent: {} (confidence: {})\n".format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence,
        )
    )
    print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))
    return response