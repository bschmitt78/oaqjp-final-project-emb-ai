import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } } 
    response = requests.post(url, json=input_json, headers=headers)
    formatted_response = json.loads(response.text)
    print(formatted_response)

    if response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotion['anger']
        disgust_score = emotion['disgust']
        fear_score = emotion['fear']
        joy_score = emotion['joy']
        sadness_score = emotion['sadness']
        dominant_emotion = max(emotion.items(), key=lambda x: x[1])
        return { 'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion }
    elif response.status_code == 400:
        return { 'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': (None, None) }
    else:
        return {'error' : 'emotion not detected', 'status_code' : response.status_code}