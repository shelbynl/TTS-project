"""auto-py2-exe
Using easy GUI this program takes a python file and returns an exe.
Additionally the file is created using a GUI
"""

import os
import easygui


MSG = "Load application..."
TITLE="App Starter"
choices = ["Google Chrome","Slack","PuTTY"]

reply = easygui.buttonbox(MSG, TITLE, choices=choices)

if reply == "Google Chrome":
    os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
elif reply == "Slack":
    os.startfile("C:\\Users\\lespo\\AppData\\Local\\slack\\slack.exe")
elif reply == "PuTTY":
    os.system("putty")
else:
    print("Execution done")
