"""Init File take one"""

import os
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig
# import azure.cognitiveservices.speech as speechsdk

KEY='cfe95862585e42b5b38dce78bff3709f'
REGION='westcentralus'


def load_credentials():
    """Loads credentials"""
    with open('credentials.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    key = lines[0].strip().split('=')[1]
    region = lines[1].strip().split('=')[1]
    return key, region


def initialize_speech_config():
    """init speech config"""
    key, region = load_credentials()
    speech_config = SpeechConfig(subscription=key, region=region)
    return speech_config


def synthesize_text(text):
    """synthesizes the text"""
    speech_config = initialize_speech_config()
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    res = synthesizer.speak_text(text)
    return res

result = synthesize_text('You plan to manually build headers \
                                                based on factors like bit depth, \
                                                sample rate, and number of channels.')
print(result)

audio = result.get_waveform()
with open('output.wav', 'wb') as f:
    f.write(audio)
