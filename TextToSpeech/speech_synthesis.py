""" speech_synthesis.py
Author:     Thaddeus Thomas
ConfigDate: 3 Dec 2022

Speech_synthesis.py is a program for configuring Text to Speech using Azure.

SPEECH_KEY is an environment variable on the host machine.

SPEECH_REGION is also an environment variable on the host machine

Jenny Neural can be changed by going to:
    <https://speech.microsoft.com/portal/voicegallery>
"""

import os
import azure.cognitiveservices.speech as speechsdk

text_file = input() # Input text files here if this step is automated
output_out = f"filename={text_file}.wav"
# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(
    subscription=os.environ.get("SPEECH_KEY"),
    region=os.environ.get("SPEECH_REGION")
)

# The language of the voice that speaks.
speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True, filename="")
speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config
)

# Get text from the console and synthesize to the default speaker.
print("Enter text to be transformed into audio")

speech_synthesis_result = speech_synthesizer.speak_text_async(text_file).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print(f"Speech synthesized for text [{text_file}]")
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print(f"Speech synthesis canceled: {cancellation_details.reason}")
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print(f"Error details: {cancellation_details.error_details}")
            print("Did you set the speech resource key and region values?")
