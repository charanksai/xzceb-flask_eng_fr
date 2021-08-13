"""Translator module that allows french and english translations using IBM Watson"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()
# Read from .env file for hitting watson's translator api
apikey = os.getenv('apikey', '')
url = os.getenv('url', 'https://api.eu-gb.language-translator.watson.cloud.ibm.com')
vrsn = os.getenv('vrsn', '2018-05-01')

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=vrsn,authenticator=authenticator)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """Converts text from English to French"""
    translation_response = language_translator.translate(text=english_text, model_id='en-fr')
    translation=translation_response.get_result()
    french_translation =translation['translations'][0]['translation']
    return french_translation

def french_to_english(french_text):
    """Converts text from French to English"""
    translation_response = language_translator.translate(text=french_text ,model_id='fr-en')
    translation=translation_response.get_result()
    english_translation = translation['translations'][0]['translation']
    return english_translation

#Invoking the methods
if __name__ == "__main__":
    TEXT = input("Enter text to see it in french: ")
    fr_text = english_to_french(TEXT)
    print("French: ", fr_text)
    en_text = french_to_english(fr_text)
    print("English: ", en_text)
