# TTS-project

Text to Speech in Azure Cloud

## Changes

Some of the changes I made include:

1. Eliminating the `os.path` and `sys` imports since they are not used.
2. Combining the **`MSG`** and **`TITLE`** variables into a single line for readability.
3. Moving the **`KEY`** and **`REGION`** environment variable retrievals to the top of the file.
4. Removing the redundant `easygui.msgbox()` call.
5. Simplifying the `main()` function by using a loop to prompt the user for their choice until they choose to exit, \
        and removing the `Path` import and `return path` statement since they are not used.
6. Separating the `get_directory()`, `get_save_file_path()`, and `get_open_file_path()` functions to make the code easier to read and maintain.
7. Refactoring the `load_credentials()` function to reduce redundancy and make it more concise.
8. Combining the `initialize_speech_config()` and `synthesize_text()` functions since they are tightly related and their code is relatively short.
9. Creating a new `save_audio_waveform()` function

## SSML

TODO: SSML Configuration
To configure SSML (Speech Synthesis Markup Language) rules into a dictionary
so that they can be automatically applied when a text-to-speech application
starts converting the text into audio.

Here are the general steps to do so:

1. **Create a dictionary**: The first step is to create a dictionary that contains the SSML rules that you want to apply.
   1. You can use any programming language to create this dictionary.
1. **Map the rules to the input text**: Once you have created the dictionary, you need to map the SSML rules to the input text.
   1. This can be done by using regular expressions or other techniques depending on your programming language.
1. **Apply the rules**: Once you have mapped the rules to the input text, you can apply the rules by using the SSML markup in your text-to-speech application.
   1. Most text-to-speech applications support SSML, and you can use the appropriate tags to apply the rules defined in your dictionary.
1. **Test and refine**: Finally, you should test your application to make sure that the SSML rules are being applied correctly.
   1. You may need to refine the rules and the mapping based on the results of your testing.
1. Overall, using a dictionary to configure SSML rules can be a powerful way to automate the application of SSML markup in your text-to-speech applications.

## Python Executable

![auto-py-2-exe][5]

### Alternate Method For Creating Executable

Might have to try this method!

```py
import os
from azure.cognitiveservices.speech import SpeechConfig, SpeechSynthesizer
from azure.cognitiveservices.speech.audio import AudioOutputConfig


KEY=<your subscription key>
REGION=<your region>


def load_credentials():
    with open('credentials.txt', 'r') as f:
        lines = f.readlines()
    key = lines[0].strip().split('=')[1]
    region = lines[1].strip().split('=')[1]
    return key, region


def initialize_speech_config():
    key, region = load_credentials()
    speech_config = SpeechConfig(subscription=key, region=region)
    return speech_config


def synthesize_text(text):
    speech_config = initialize_speech_config()
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    result = synthesizer.speak_text(text)
    return result


result = synthesize_text('Hello, world!')
print(result)


audio = result.get_waveform()
with open('output.wav', 'wb') as f:
    f.write(audio)
```

## Various Links

- [AI-102][1]
- [AI-102 00][2]
- [AI-102 07][3]
- [Transcribe Speech][4]
- [TTS Price per word][6]
- [Azure Documentation][7]
- [Speech Service][8]

## Export Environment Variables

```bash
PROJECT_ID = <input pid>
FILE_NAME = <input filename>
export PROJECT_ID=$PROJECT_ID
export FILE_NAME=$FILE_NAME
scripts/dashboard/dashboard.sh import $PROJECT_ID $FILE_NAME
```

## Alternate Method

```bash
setx SPEECH_REGION
set SPEECH_KEY
```

## Directory

```cmd
D:.
├───.github
│   └───ISSUE_TEMPLATE
├───.venv
│   ├───Include
│   ├───Lib
│   │   └───site-packages
│   │       ├───pip
│   │       │   ├───_internal
│   │       │   │   ├───cli
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───commands
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───distributions
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───index
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───locations
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───metadata
│   │       │   │   │   ├───importlib
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───models
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───network
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───operations
│   │       │   │   │   ├───build
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───install
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───req
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───resolution
│   │       │   │   │   ├───legacy
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───resolvelib
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───utils
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───vcs
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   ├───_vendor
│   │       │   │   ├───cachecontrol
│   │       │   │   │   ├───caches
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───certifi
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───chardet
│   │       │   │   │   ├───cli
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───metadata
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───colorama
│   │       │   │   │   ├───tests
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───distlib
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───distro
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───idna
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───msgpack
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───packaging
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───pkg_resources
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───platformdirs
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───pygments
│   │       │   │   │   ├───filters
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───formatters
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───lexers
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───styles
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───pyparsing
│   │       │   │   │   ├───diagram
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───pyproject_hooks
│   │       │   │   │   ├───_in_process
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───requests
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───resolvelib
│   │       │   │   │   ├───compat
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───rich
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───tenacity
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───tomli
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───urllib3
│   │       │   │   │   ├───contrib
│   │       │   │   │   │   ├───_securetransport
│   │       │   │   │   │   │   └───__pycache__
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───packages
│   │       │   │   │   │   ├───backports
│   │       │   │   │   │   │   └───__pycache__
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   ├───util
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───webencodings
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───pip-23.0.1.dist-info
│   │       ├───pkg_resources
│   │       │   ├───extern
│   │       │   │   └───__pycache__
│   │       │   ├───_vendor
│   │       │   │   ├───importlib_resources
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───jaraco
│   │       │   │   │   ├───text
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───more_itertools
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───packaging
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───pyparsing
│   │       │   │   │   ├───diagram
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───setuptools
│   │       │   ├───command
│   │       │   │   └───__pycache__
│   │       │   ├───config
│   │       │   │   ├───_validate_pyproject
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   ├───extern
│   │       │   │   └───__pycache__
│   │       │   ├───_distutils
│   │       │   │   ├───command
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   ├───_vendor
│   │       │   │   ├───importlib_metadata
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───importlib_resources
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───jaraco
│   │       │   │   │   ├───text
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───more_itertools
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───packaging
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───pyparsing
│   │       │   │   │   ├───diagram
│   │       │   │   │   │   └───__pycache__
│   │       │   │   │   └───__pycache__
│   │       │   │   ├───tomli
│   │       │   │   │   └───__pycache__
│   │       │   │   └───__pycache__
│   │       │   └───__pycache__
│   │       ├───setuptools-65.5.0.dist-info
│   │       └───_distutils_hack
│   │           └───__pycache__
│   └───Scripts
├───Documentation
├───exe-config
├───output
│   └───easy_gui
│       ├───numpy
│       │   ├───core
│       │   ├───fft
│       │   ├───linalg
│       │   └───random
│       ├───PIL
│       ├───psutil
│       ├───tcl
│       │   ├───encoding
│       │   ├───http1.0
│       │   ├───msgs
│       │   ├───opt0.4
│       │   └───tzdata
│       │       ├───Africa
│       │       ├───America
│       │       │   ├───Argentina
│       │       │   ├───Indiana
│       │       │   ├───Kentucky
│       │       │   └───North_Dakota
│       │       ├───Antarctica
│       │       ├───Arctic
│       │       ├───Asia
│       │       ├───Atlantic
│       │       ├───Australia
│       │       ├───Brazil
│       │       ├───Canada
│       │       ├───Chile
│       │       ├───Etc
│       │       ├───Europe
│       │       ├───Indian
│       │       ├───Mexico
│       │       ├───Pacific
│       │       ├───SystemV
│       │       └───US
│       ├───tcl8
│       │   ├───8.4
│       │   │   └───platform
│       │   ├───8.5
│       │   └───8.6
│       └───tk
│           ├───images
│           ├───msgs
│           └───ttk
├───scraper
└───text_to_speech
    ├───master
    ├───old
    └───__pycache__
```

[1]: <https://microsoftlearning.github.io/AI-102-AIEngineer/> "MAster exercise shell for AI-900"
[2]: <https://microsoftlearning.github.io/AI-102-AIEngineer/Instructions/00-setup.html> "Exercise 00 for AI900"
[3]: <https://microsoftlearning.github.io/AI-102-AIEngineer/Instructions/07-speech.html> "This si the actual Spech Exercise"
[4]: <https://learn.microsoft.com/en-us/training/modules/transcribe-speech-input-text/7-exercise-speech-app> "training Module from Microsoft Learn for Speech exercise"
[5]: <./Documentation/pic1.png> "This is the module that is used to create the Executable"
[6]: <./Documentation/VTT_Pricing.xlsx> "Speech cognitive service use rate"
[7]: <./Documentation/azure-cognitive-services-speech-service.pdf> "Documentation on all of the cognitive cloud services"
[8]: <./Documentation/Speech%20Service%20Documentation.pdf> "Speech Service Documentation"
