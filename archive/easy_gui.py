"""
Creates the box for our executable
# need titles for the execution in the GUI
# TODO: need command line for inputting text in GUI
# need __init__ file for the python directory to compile everything before the py too exe is run
"""


import sys
import os
import os.path
import easygui


MSG = "Load application..."
TITLE = "Text-to-Speech Audio ReImagination"  # TSAR I
CHOICES = ["Create Audio File", ".", "Exit"]

easygui.ynbox(MSG, TITLE, ("Yes", "No"))
# easygui.msgbox("This is a basic message box.", TITLE)


def main():
    """
    Runs the main application
    """
    rep = resource_path("./synthesizer.py")
    path = os.path.relpath(rep)
    reply = easygui.buttonbox(MSG, TITLE, CHOICES)
    if reply == CHOICES[0]:
        num1 = os.startfile(path)
        return path
    if reply == CHOICES[1]:
        num1 = os.startfile(path)
        return num1
    else:
        os.system("Exit")
        exit()


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


if __name__ == "__main__":
    main()
