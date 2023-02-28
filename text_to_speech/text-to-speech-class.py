"""Final Version of text-to-speech before conversion to an exe"""

import os
import sys
import easygui
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig

class TTS:
    def __init__(self):
        self.key = os.environ.get('SP_KEY')
        if self.key is None:
            raise ValueError('SP_KEY environment variable is not set.')
        self.region = os.environ.get('SP_REG')
        if self.region is None:
            raise ValueError('SP_REG environment variable is not set.')
        self.speech_config = self.initialize_speech_config()

    def __repr__(self):
        return f"TTS(key={self.key}, region={self.region})"

    def __str__(self):
        return f"Text-to-Speech object with key {self.key} and region {self.region}"

    def resource_path(self, relative_path):
        """
        Get the absolute path to the resource,
        works for dev and for PyInstaller
        <https://pyinstaller.org/en/stable/runtime-information.html>
        """
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    @staticmethod
    def get_directory():
        """Get the directory path of the files to convert"""
        return easygui.diropenbox()

    @staticmethod
    def get_save_file_path():
        """Get the save file path for the audio output"""
        return easygui.filesavebox()

    @staticmethod
    def get_open_file_path():
        """Get the path of a file to convert"""
        return easygui.fileopenbox()

    @staticmethod
    def get_user_choice():
        """Get user choice for how to input files"""
        choices = ["Directory", "Save File", "Open File", "Exit"]
        return easygui.buttonbox(
            "Select files to convert, then select where to save the output",
            "Text-to-Speech Audio ReImagination (TSAR I)",
            choices,)

    def initialize_speech_config(self):
        """Initialize and return a SpeechConfig object for the Speech service"""
        speech_config = SpeechConfig(subscription=self.key, region=self.region)
        return speech_config

    def convert_file_to_audio(self, file_path, output_file_path):
        """Convert a file to audio"""
        audio_config = AudioOutputConfig(filename=f"{output_file_path}.wav")
        synthesizer = SpeechSynthesizer(
            speech_config=self.speech_config, audio_config=audio_config
        )
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        synthesizer.speak_text_async(text).get()

    def convert_files_to_audio(self, input_file_paths, output_file_path):
        """Convert multiple files to audio"""
        audio_config = AudioOutputConfig(filename=f"{output_file_path}.wav")
        synthesizer = SpeechSynthesizer(
            speech_config=self.speech_config, audio_config=audio_config
        )
        for file_path in input_file_paths:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
            synthesizer.speak_text_async(text).get()

    def main(self):
        """Runs the main function of the TTS Class"""
        while True:
            choice = self.get_user_choice()
            if choice == "Directory":
                directory_path = self.get_directory()
                if directory_path:
                    output_file_path = self.get_save_file_path()
                    if output_file_path:
                        input_file_paths = [
                            os.path.join(directory_path, file)
                            for file in os.listdir(directory_path)
                            if file.endswith(".txt")
                        ]
                        self.convert_files_to_audio(input_file_paths, output_file_path)
            elif choice == "Save File":
                input_file_path = self.get_open_file_path()
                if input_file_path:
                    output_file_path = self.get_save_file_path()
                    if output_file_path:
                        self.convert_file_to_audio(input_file_path, output_file_path)
            elif choice == "Open File":
                input_file_path = self.get_open_file_path()
                if input_file_path:
                    output_file_path = self.get_save_file_path()
                    if output_file_path:
                        self.convert_file_to_audio(input_file_path, output_file_path)
            else:
                break

if __name__=="__main__":
    tts = TTS()
    tts.main()
