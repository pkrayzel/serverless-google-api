import json
import os

from google.cloud import texttospeech
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
from google.cloud import translate_v3


def translate_text(text, target='en'):
    """
    Target must be an ISO 639-1 language code.
    https://cloud.google.com/translate/docs/languages
    """
    client = translate_v3.TranslationServiceClient()
    result = client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))

    return result


def hello(event, context):
    credentials = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "key")
    # something to do with credentials

    example_text = "Hola amigos"
    translation = translate_text(example_text, target='en')

    body = {
        "source_message": example_text,
        "message": translation,
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
    }

    return response


# running locally
if __name__ == "__main__":
    hello(None, None)
