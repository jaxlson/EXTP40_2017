'''
Created on 30 nov. 2017

@author: Josefine
'''
from Tkinter import StringVar
import ttk

class ComboBox(object):

    def __init__(self, frame):
        box_value = StringVar()
        self.box = ttk.Combobox(frame, textvariable=box_value, state='readonly')
        self.box['values'] = ('jet', 'parula', 'hsv','hot','cool',
                              'spring','summer','autumn','winter',
                              'grey','bone','copper','pink','colorcube')
        
        self.box.bind("<<ComboboxSelected>>", self.select_cmap)
        self.box.current(0)
        self.box.pack()
    
    def select_cmap(self, event):
            print(self.box.get())    