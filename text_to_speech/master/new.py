"""
Synthesizes speech for Microsoft Azure cognitive services speech platform
Part of Speech SDK offered by Microsoft.
Reconfigured and appropriated by Thad Thomas Dec 10. 2022
"""


import os
from pathlib import Path
import easygui
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig


# The language of the voice that speaks.
VOICE = "en-US-JennyNeural"
MSG = "Load application..."
TITLE = "Text-to-Speech Audio ReImagination (TSAR I)"
KEY = os.environ.get("SP_KEY")
REGION = os.environ.get("SP_REG")


def get_directory():
    return easygui.diropenbox()


def get_save_file_path():
    return easygui.filesavebox()


def get_open_file_path():
    return easygui.fileopenbox()


def get_user_choice():
    choices = ['Directory', 'Save File', 'Open File', 'Exit']
    return easygui.buttonbox(MSG, TITLE, choices)


def load_credentials():
    with open('credentials.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        key = lines[0].strip().split('=')[1]
        region = lines[1].strip().split('=')[1]
    return os.environ.get(KEY, key), os.environ.get(REGION, region)


def initialize_speech_config():
    key, region = load_credentials()
    speech_config = SpeechConfig(subscription=key, region=region)
    return speech_config


def speech_synthesizer_bookmark_reached_cb(evt: speechsdk.SessionEventArgs):
    """defines the point when a bookmark has been reached in the voice synthesis"""
    print("BookmarkReached event:")
    print(f"\tAudioOffset: {(evt.audio_offset + 5000) / 10000}ms")
    print(f"\tText: {evt.txt}")


def speech_synthesizer_synthesis_canceled_cb(evt: speechsdk.SessionEventArgs):
    """Returns that synthesis was canceled"""
    print("SynthesisCanceled event")


def speech_synthesizer_synthesis_completed_cb(evt: speechsdk.SessionEventArgs):
    """Returns that synthesis has finished"""
    print("SynthesisCompleted event:")
    print(f"\tAudioData: {len(evt.result.audio_data)} bytes")
    print(f"\tAudioDuration: {evt.result.audio_duration}")


def speech_synthesizer_synthesis_started_cb(evt: speechsdk.SessionEventArgs):
    """returns that speech has started"""
    print("SynthesisStarted event") # needs to call the evt variable


def speech_synthesizer_synthesizing_cb(evt: speechsdk.SessionEventArgs):
    """The Synthesizer is Synthesizing"""
    print("Synthesizing event:")
    print(f"\tAudioData: {len(evt.result.audio_data)} bytes")


def speech_synthesizer_viseme_received_cb(evt: speechsdk.SessionEventArgs):
    """Viseme ID was received"""
    print("VisemeReceived event:")
    print(f"\tAudioOffset: {(evt.audio_offset + 5000) / 10000}ms")
    print(f"\tVisemeId: {evt.viseme_id}")


def speech_synthesizer_word_boundary_cb(evt: speechsdk.SessionEventArgs):
    """Informs the user about approaching the 5000 character limit per file"""
    print(
        f"""WordBoundary event:\n
            \tBoundaryType: {evt.boundary_type}\n
            \tAudioOffset: {(evt.audio_offset + 5000) / 10000}ms\n
            \tDuration: {evt.duration}\n
            \tText: {evt.text}\n
            \tTextOffset: {evt.text_offset}\n
            \tWordLength: {evt.word_length}"""
    )


# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(
    subscription=os.environ.get("SPEECH_KEY"),
    region=os.environ.get("SPEECH_REGION")
)

# Required for WordBoundary event sentences.
speech_config.set_property(
    property_id=speechsdk.PropertyId.SpeechServiceResponse_RequestSentenceBoundary,
    value="true",
)
audio_config = speechsdk.audio.AudioOutputConfig(filename="audio_output.wav")
speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config, audio_config=audio_config
)

# Subscribe to events
speech_synthesizer.bookmark_reached.connect(speech_synthesizer_bookmark_reached_cb)
speech_synthesizer.synthesis_canceled.connect(speech_synthesizer_synthesis_canceled_cb)
speech_synthesizer.synthesis_completed.connect(
    speech_synthesizer_synthesis_completed_cb
)
speech_synthesizer.synthesis_started.connect(speech_synthesizer_synthesis_started_cb)
speech_synthesizer.synthesizing.connect(speech_synthesizer_synthesizing_cb)
speech_synthesizer.viseme_received.connect(speech_synthesizer_viseme_received_cb)
speech_synthesizer.synthesis_word_boundary.connect(speech_synthesizer_word_boundary_cb)


SSML = f"""<speak version='1.0' \
    xml:lang='en-US' \
    xmlns='http://www.w3.org/2001/10/synthesis'\
    xmlns:mstts='http://www.w3.org/2001/mstts'>
    <voice name='{VOICE}'>
    <mstts:viseme type='redlips_front'/>\
        The rainbow has seven colors: \
    <bookmark mark='colors_list_begin'/>\
    Red, orange, yellow, green, blue, indigo, and violet.\
    <bookmark mark='colors_list_end'/>.
    </voice>
    </speak>"""

# Synthesize the SSML
print(f"SSML to synthesize: \r\n{SSML}")
speech_synthesis_result = speech_synthesizer.speak_ssml_async(SSML).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("SynthesizingAudioCompleted result")
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print(f"Speech synthesis canceled: {cancellation_details.reason}")
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print(f"Error details: {cancellation_details.error_details}")
            print("Did you set the speech resource key and region values?")

def synthesize_text(text):
    speech_config = initialize_speech_config()
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    res = synthesizer.speak_text(text)
    return res


def save_audio_waveform(audio):
    with open('output.wav', 'wb') as f:
        f.write(audio)


def main():
    while True:
        choice = get_user_choice()
        if choice == 'Directory':
            directory = get_directory()
            if directory:
                print(f"Selected directory: {directory}")
        elif choice == 'Save File':
            file_save = get_save_file_path()
            if file_save:
                print(f"Selected save file path: {file_save}")
        elif choice == 'Open File':
            file_open = get_open_file_path()
            if file_open:
                print(f"Selected open file path: {file_open}")
        else:
            print("Exiting the application...")
            break
    if directory:
        result = synthesize_text("Hello, world!")
        print(result)
        audio = result.get_waveform()
        save_audio_waveform(audio)


if __name__ == '__main__':
    main()
