"""Test module that allows to test french and english translations using IBM Watson"""

import unittest
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from machinetranslation.translator import english_to_french, french_to_english

load_dotenv()
# Read from .env file for hitting watson's translator api
apikey = os.environ['apikey']
url = os.environ['url']
vrsn = os.environ['vrsn']

# create an instance of Language Translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=vrsn,authenticator=authenticator)
language_translator.set_service_url(url)



class TestEnglishToFrench(unittest.TestCase):
    def test_pass_e2f(self):
        self.assertEqual(english_to_french(language_translator, "Hello"),"Bonjour")
    
    @unittest.expectedFailure
    def test_fail_e2f(self):
        self.assertRaises(ValueError, english_to_french(language_translator, None))

class TestFrenchToEnglish(unittest.TestCase):
    def test_pass_f2e(self):
        self.assertEqual(french_to_english(language_translator, "Bonjour"),"Hello")

    @unittest.expectedFailure
    def test_fail_f2e(self):
        self.assertRaises(ValueError,french_to_english(language_translator, None))

unittest.main()
