''' Emotion Detection Final Project
'''
import json
import requests

def emotion_detector(text_to_analyze):
    ''' Function to detect emotion with the use of the Watson API
    '''
    # Define the URL for the sentiment analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    payload = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=payload, headers=header)

    # Return the Text
    return response.text