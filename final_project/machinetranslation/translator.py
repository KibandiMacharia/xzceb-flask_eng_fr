"""System module."""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()


#apikey = os.environ['apikey']
#url = os.environ['url']

myauthenticator = IAMAuthenticator('jwIUFEcrQ6HTkhQtWqDggKZScglipt6SNSlhpy6_i8vo')
language_translator = LanguageTranslatorV3(
    version='{version}',
    authenticator=myauthenticator
)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/d0134edc-90eb-434e-bdfb-fc66ca90a38c')

language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """function to translate english to french."""
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """function to translate french to english."""
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")

