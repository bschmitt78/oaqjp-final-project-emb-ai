from emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
	
        # Test case for joy emotion
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result[result['dominant_emotion'][0]], result['joy'])
        
        # Test case for anger emotion
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result[result['dominant_emotion'][0]], result['anger'])
        
        # Test case for disgust emotion
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result[result['dominant_emotion'][0]], result['disgust'])
        
        # Test case for sadness emotion
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result[result['dominant_emotion'][0]], result['sadness'])
        
        # Test case for fear emotion
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result[result['dominant_emotion'][0]], result['fear'])

unittest.main()