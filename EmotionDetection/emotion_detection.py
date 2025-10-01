'''
    This package will detects emotions using IBM Watson NPL library
'''

import requests

'''
    emotion_detector function will send the text to analyzie using
    requests python library
    params:
        test_to_analyze - string

    retrun -> dictionary: 
        label - string
        score - floar
'''
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
    input = {
        "raw_document": { 
            "text": text_to_analyze 
        }
    }
    response = requests.post(url, headers=header, json=input)

    if response.status_code == 400 :
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }
    formatted_response = response.json()
    result = formatted_response["emotionPredictions"][0]['emotion']
    result["dominant_emotion"] = max(result, key=result.get)
    return result
