'''
Created on 28 nov. 2017

@author: Josefine
'''
from Tkinter import Label, Entry, Scale, HORIZONTAL

class FrameScale(object):
 
    def __init__(self, master, frame):
        self.min_label = Label(frame, text = "Min.")
        self.max_label = Label(frame, text = "Max.")
        self.min_entry = Entry(frame)
        self.max_entry = Entry(frame)
        self.min_scale = Scale(frame, orient=HORIZONTAL)
        self.max_scale = Scale(frame, orient=HORIZONTAL)
        
        self.min_label.grid(row=0, column=0)
        self.max_label.grid(row=1, column=0)
        self.min_entry.grid(row=0, column=1)
        self.max_entry.grid(row=1, column=1)
        self.min_scale.grid(row=0, column=2)
        self.max_scale.grid(row=1, column=2)
        
        
        