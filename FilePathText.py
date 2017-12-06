from Tkinter import Text, INSERT

class FilePathText(object):


    def __init__(self, master):
        text = Text(master)
        text.insert(INSERT, "test")