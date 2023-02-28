"""Init File take one"""

import sys
import os
import os.path
from pathlib import Path
import easygui
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig


# path = os.path.relpath(p)
KEY= os.environ.get("SP_KEY")
REGION=os.environ.get("SP_REG")
MSG = "Load application..."
TITLE="Text-to-Speech Audio ReImagination" # TSAR I

easygui.ynbox(MSG, TITLE, ('Yes', 'No'))

# easygui.msgbox('This is a basic message box.', TITLE)
# need titles for the execution in the GUI
# need command line for inputting text in GUI
# need __init__ file for the python directory to compile everything before the py too exe is run

def main():
    """
    runs the main application
    """
    directory = easygui.diropenbox()
    file_save = easygui.filesavebox()
    file_open = easygui.fileopenbox()
    path = Path('./synthesizer.py')
    choices = ['Directory','Save File', 'Open File', 'Exit']
    reply = easygui.buttonbox(MSG, TITLE, choices)

    if reply == choices[0]:
        return directory
    elif reply == choices[1]:
        return file_save
    elif reply == choices[2]:
        return file_open
    else:
        os.system("Exit")
        return path


def load_credentials():
    """Loads credentials"""
    with open('credentials.txt', 'r', encoding='utf-8') as f1:
        lines = f1.readlines()
    key = lines[0].strip().split('=')[1]
    region = lines[1].strip().split('=')[1]
    return key, region


def initialize_speech_config():
    """init speech config"""
    key, region = load_credentials()
    speech_config = SpeechConfig(subscription=os.environ.get(KEY,key),
    region=os.environ.get(REGION, region))
    return speech_config


def synthesize_text(text):
    """synthesizes the text"""
    speech_config = initialize_speech_config()
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    res = synthesizer.speak_text(text)
    return res


def resource_path(relative_path):
    """
    Get the absolute path to the resource,
    works for dev and for PyInstaller
    """
    try:# PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__=='__main__':
    main()
    result = synthesize_text()
    print(result)
    audio = result.get_waveform()
    with open('output.wav', 'wb') as f:
        f.write(audio)
