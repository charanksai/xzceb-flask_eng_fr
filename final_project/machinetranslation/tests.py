"""Test module that allows to test french and english translations using IBM Watson"""

import unittest
from . import translator 

class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french_assert_equal(self):
        self.assertEqual(translator.english_to_french("Hello"),"Bonjour")
    
    def test(self):
        self.assertNotEqual(translator.english_to_french("None"), "")
        
    @unittest.expectedFailure
    def test_english_to_french_assert_not_equal(self):
        self.assertNotEqual(translator.english_to_french(None), "")

class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english_assert_equal(self):
        self.assertEqual(translator.french_to_english("Bonjour"),"Hello")

    def test(self):
        self.assertNotEqual(translator.french_to_english("None"), "")

    @unittest.expectedFailure
    def test_french_to_english_assert_not_equal(self):
        self.assertNotEqual(translator.french_to_english(None), "")

if __name__ == "__main__":
    unittest.main()