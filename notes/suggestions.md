Here are a few suggestions to make the code more pythonic:

Remove unnecessary variables: The self.path variable in the __path__ method is not being used anywhere in the code. You can remove this variable.

Use pathlib.Path instead of os.path: In the convert_file_to_audio and convert_files_to_audio methods, you can use pathlib.Path instead of os.path to manipulate file paths. For example, instead of using os.path.join(directory_path, file) to join a directory path and a file name, you can use Path(directory_path) / file.

Use list comprehension: In the convert_files_to_audio method, you can use a list comprehension instead of a for loop to create the input_file_paths list. For example, instead of using:

```py
input_file_paths = []
for file in os.listdir(directory_path):
    if file.endswith(".txt"):
        input_file_paths.append(os.path.join(directory_path, file))
```

you can use:

```py
input_file_paths = [Path(directory_path) / file for file in os.listdir(directory_path) if file.endswith(".txt")]
```

Use with statement: In the load_credentials method, you can use a with statement to open the credentials file instead of using file = open("credentials.txt", "r", encoding="utf-8"). The with statement automatically closes the file when you are done with it. For example, you can use:


```py
with open("credentials.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    key = lines[0].strip().split("=")[1]
    region = lines[1].strip().split("=")[1]
```


Use f-strings: In the convert_file_to_audio and convert_files_to_audio methods, you can use f-strings to format the output file name instead of using string concatenation. For example, instead of using filename=f'{output_file_path}.wav', you can use filename=f"{output_file_path}.wav".

Use more descriptive names: Some of the variable names in the code are not very descriptive. For example, tts can be renamed to text_to_speech or speech_synthesizer.

Use `if __name__ == "__main__"` guard: You can use the `if __name__ == "__main__"` guard to ensure that the code inside it only runs when the script is run directly and not when it is imported as a module. For example, you can use:

   ```py
   if __name__ == "__main__":
       tts = TTS()
       tts.main()
   ```

This prevents the code from running if the script is imported as a module.

## Here's the updated code with these suggestions:

```py
import os
import sys
from pathlib import Path
import easygui
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig


class TTS:
    def __init__(self):
        self.key, self.region = self.load_credentials()
        self.speech_config = self.initialize_speech_config()

    def __path__(self):
        return Path("SP_KEY", "SP_REG")

    def resource_path(self, relative_path):
        """
        Get the absolute path to the resource,
        works for dev and for PyInstaller
        <https://pyinstaller.org/en/stable/runtime-information.html>
        """
        try:
            # PyInstaller creates
```
