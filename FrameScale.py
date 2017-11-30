'''
Created on 28 nov. 2017

@author: Josefine
'''
from Tkinter import Label, Entry, Scale, HORIZONTAL, IntVar, END
import numpy as np

class FrameScale(object):
 
    def __init__(self, a, frame):
        max = np.amax(a)
        min = np.amin(a)
        self.min_var = IntVar()
        self.max_var = IntVar()
        
        self.min_label = Label(frame, text = "Min.")
        self.max_label = Label(frame, text = "Max.")
        self.min_entry = Entry(frame, textvariable=self.min_var)
        self.max_entry = Entry(frame, textvariable=self.max_var)
        self.min_entry.bind("<Return>", 
                            lambda event: entry_change(self.min_scale,self.min_var.get()))
        self.max_entry.bind("<Return>", 
                            lambda event: entry_change(self.max_scale,self.max_var.get()))
        
        def min_change(val):
            self.min_var.set(val)
        
        def max_change(val):
            self.max_var.set(val)
            
        self.min_scale = Scale(frame, orient=HORIZONTAL, from_=min, to=max-1, command=min_change)
        self.max_scale = Scale(frame, orient=HORIZONTAL, from_=min+1, to=max, command=max_change)
        
        self.min_label.grid(row=0, column=0)
        self.max_label.grid(row=1, column=0)
        self.min_entry.grid(row=0, column=1)
        self.max_entry.grid(row=1, column=1)
        self.min_scale.grid(row=0, column=2)
        self.max_scale.grid(row=1, column=2)
        
        def entry_change(scale, value):
            scale.configure(from_=value-20, to=value+20)
            scale.set(value)
        
        def check_values(min,max):
            # Min should not be greater then Max (Min -> Max-1)
            # Max should not be smaller then Min (Max -> Min+1)
            pass
        