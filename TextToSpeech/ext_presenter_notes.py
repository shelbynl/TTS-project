"""
Extract Presenter Notes
TODO: #2 add menu to main function
TODO: #3 add location to save text to
TODO: #4 add method for multiple files
TODO: #5 make FILE an input with type checking

REFERENCE:
<https://stackoverflow.com/questions/63659972/extract-presenter-notes-from-pptx-file-powerpoint>
"""

import collections.abc
from pptx import Presentation
import pandas as pd

FILE = \
    'D:/Student_Assistant/CareerNavigation/New-Slides/02-CS9101.pptx'
PPT=Presentation(FILE)

def main():
    """runs the main function of the program"""
    lst = enum_notes()
    with open(file='FILE', mode='w', encoding='utf-8') as file_out:
        df = pd.DataFrame(lst)
        df.to_csv(file_out)

def enum_notes():
    """Enumerates the notes and returns the text"""
    notes = []
    for page, slide in enumerate(PPT.slides):
        text_note = slide.notes_slide.notes_text_frame.text
        notes.append((page, text_note))
    return notes

def enum_slides():
    """Enumerates the slides for text"""
    notes = []
    for page, slide in enumerate(PPT.slides):
        temp = []
        for shape in slide.shapes:
            # this will extract all text in text boxes on the slide.
            if shape.has_text_frame and shape.text.strip():
                temp.append(shape.text)
        notes.append((page, temp))
    return notes

if __name__=='__main__':
    main()
