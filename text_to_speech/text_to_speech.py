"""Final Version of text-to-speech before conversion to an exe"""

import os
import sys
import easygui
import _collections_abc
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig

# C:/Users/Thaddeus Maximus/AppData/Roaming/Python/Python311/site-packages/win32/win32api.pyd
# C:/Users/Thaddeus Maximus/AppData/Roaming/Python/Python311/site-packages/win32/win32pdh.pyd

def resource_path(relative_path):
    """
    Get the absolute path to the resource,
    works for dev and for PyInstaller
    <https://pyinstaller.org/en/stable/runtime-information.html>
    """
    try:# PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_directory():
    """Get the directory path of the files to convert"""
    return easygui.diropenbox()


def get_save_file_path():
    """Get the save file path for the audio output"""
    return easygui.filesavebox()


def get_open_file_path():
    """Get the path of a file to convert"""
    return easygui.fileopenbox()


def get_user_choice():
    """Get user choice for how to input files"""
    choices = ["Directory", "Save File", "Open File", "Exit"]
    return easygui.buttonbox(
        "Choose how to select files to convert",
        "Text-to-Speech Audio ReImagination (TSAR I)",
        choices,
    )


def load_credentials():
    """Load Speech service credentials from the credentials.txt file"""
    with open("credentials.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        key = lines[0].strip().split("=")[1]
        region = lines[1].strip().split("=")[1]
    return os.environ.get("SP_KEY", key), os.environ.get("SP_REG", region)


def initialize_speech_config():
    """Initialize and return a SpeechConfig object for the Speech service"""
    key, region = load_credentials()
    speech_config = SpeechConfig(subscription=key, region=region)
    return speech_config


def convert_file_to_audio(file_path, output_file_path):
    """Convert a file to audio"""
    speech_config = initialize_speech_config()
    audio_config = AudioOutputConfig(filename=f'{output_file_path}.wav')
    synthesizer = SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config
    )
    with open(file_path, "r", encoding='utf-8') as file:
        text = file.read()
    synthesizer.speak_text_async(text).get()


def convert_files_to_audio(input_file_paths, output_file_path):
    """Convert multiple files to audio"""
    speech_config = initialize_speech_config()
    audio_config = AudioOutputConfig(filename=f'{output_file_path}.wav')
    synthesizer = SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config
    )
    for file_path in input_file_paths:
        with open(file_path, "r", encoding='utf-8') as file:
            text = file.read()
        synthesizer.speak_text_async(text).get()


def main():
    """Main function"""
    while True:
        choice = get_user_choice()
        if choice == "Directory":
            directory_path = get_directory()
            if directory_path:
                output_file_path = get_save_file_path()
                if output_file_path:
                    input_file_paths = [
                        os.path.join(directory_path, file)
                        for file in os.listdir(directory_path)
                        if file.endswith(".txt")
                    ]
                    convert_files_to_audio(input_file_paths, output_file_path)
        elif choice == "Save File":
            input_file_path = get_open_file_path()
            if input_file_path:
                output_file_path = get_save_file_path()
                if output_file_path:
                    convert_file_to_audio(input_file_path, output_file_path)
        elif choice == "Open File":
            input_file_path = get_open_file_path()
            if input_file_path:
                output_file_path = get_save_file_path()
                if output_file_path:
                    convert_file_to_audio(input_file_path, output_file_path)
        else:
            break


if __name__ == "__main__":
    main()
