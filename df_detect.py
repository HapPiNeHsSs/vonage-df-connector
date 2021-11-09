from google.cloud import dialogflow
SAMPLE_RATE = 16000
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