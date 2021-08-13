"""Translator module that allows french and english translations using IBM Watson"""
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()
# Read from .env file for hitting watson's translator api
apikey = os.getenv('apikey')
url = os.getenv('url')
vrsn = os.getenv('vrsn')

# create an instance of Language Translator
def instance():
    """Creates Instance of Language Translator"""
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(version=vrsn,authenticator=authenticator)
    language_translator.set_service_url(url)
    return language_translator

def english_to_french(language_translator, english_text):
    """Converts text from English to French"""
    translation_response = language_translator.translate(text=english_text, model_id='en-fr')
    translation=translation_response.get_result()
    french_translation =translation['translations'][0]['translation']
    return french_translation

def french_to_english(language_translator, french_text):
    """Converts text from French to English"""
    translation_response = language_translator.translate(text=french_text ,model_id='fr-en')
    translation=translation_response.get_result()
    english_translation = translation['translations'][0]['translation']
    return english_translation

#Invoking the methods
tr_instance = instance()
TEXT = "Hello World, How is everything going?"
fr_text = english_to_french(tr_instance, TEXT)
print(fr_text)
en_text = french_to_english(tr_instance, fr_text)
print(en_text)
