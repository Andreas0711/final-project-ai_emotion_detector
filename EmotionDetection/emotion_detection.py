''' Emotion Detection Final Project
'''
import json
import requests

def emotion_detector(text_to_analyze):
    ''' Function to detect emotion with the use of the Watson API
    '''
    # Define the URL for the sentiment analysis API
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )

    # Create the payload with the text to be analyzed
    payload = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=payload, headers=header, timeout=10)

    # If status-code 400, an empty dictionary will be returned
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # Extraction of Information
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Find the emotion with the highest score
    result = {
              'anger': anger_score,
              'disgust': disgust_score,
              'fear': fear_score,
              'joy': joy_score,
              'sadness': sadness_score
             }
    try:
        dominant_emotion = max(result, key=result.get)
    except (TypeError, ValueError):
        dominant_emotion = None

    result['dominant_emotion'] = dominant_emotion

    # Return the result dictionary
    return result
