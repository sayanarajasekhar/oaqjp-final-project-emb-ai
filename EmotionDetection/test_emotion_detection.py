import unittest
from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    '''
        Test Emotion Detector
    '''
    def test_joy(self):
        '''
            Testing joy emotion
        '''
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response["dominant_emotion"], 'joy')
    def test_anger(self):
        '''
            Testing anger emotion
        '''
        response = emotion_detector("I am really mad about this")
        self.assertEqual(response["dominant_emotion"], 'anger')
    def test_disgust(self):
        '''
            Testing disgust emotion
        '''
        response = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response["dominant_emotion"], 'disgust')
    def test_sadness(self):
        '''
            Testing sadness emotion
        '''
        response = emotion_detector("I am so sad about this")
        self.assertEqual(response["dominant_emotion"], 'sadness')
    def test_fear(self):
        '''
            Testing fear emotion
        '''
        response = emotion_detector("I am really afraid that this will happen	")
        self.assertEqual(response["dominant_emotion"], 'fear')

if __name__ == "__main__":
    unittest.main()