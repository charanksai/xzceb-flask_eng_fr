"""Test module that allows to test french and english translations using IBM Watson"""

import unittest
from . import translator 

class TestEnglishToFrench(unittest.TestCase):
    def test_pass_e2f(self):
        self.assertEqual(translator.english_to_french("Hello"),"Bonjour")
    
    @unittest.expectedFailure
    def test_fail_e2f(self):
        self.assertNotEqual(translator.english_to_french(None), "")

class TestFrenchToEnglish(unittest.TestCase):
    def test_pass_f2e(self):
        self.assertEqual(translator.french_to_english("Bonjour"),"Hello")

    @unittest.expectedFailure
    def test_fail_f2e(self):
        self.assertNotEqual(translator.french_to_english(None), "")

if __name__ == "__main__":
    unittest.main()
