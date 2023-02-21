"""Creates the box for our executable"""

import os
import easygui

MSG = "Load application..."
TITLE="Text-to-Speech Audio ReImagination" # TSAR I
CHOICES = ["Create Audio","Add Text","Exit"]

# TODO: need titles for the execution in the GUI
# TODO: need command line for inputting text in GUI
# TODO: need __init__ file for the python directory to compile everything before the py too exe is run

def main():
    """runs the main application"""
    reply = easygui.buttonbox(MSG, TITLE, CHOICES)
    if reply == CHOICES[0]:
        demo = os.startfile("Demo_synthesizer.py")
        return demo
    if reply == "CHOICES[1]":
        os.system("")
    else:
        os.system("Exit")
        return

if __name__=='__main__':
    main()
