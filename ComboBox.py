'''
Created on 30 nov. 2017

@author: Josefine
'''
from Tkinter import StringVar
import ttk

class ComboBox(object):

    def __init__(self, frame, map_):
        self.map = map_
        box_value = StringVar()
        self.box = ttk.Combobox(frame, textvariable=box_value, state='readonly')
        self.box['values'] = ('jet','hsv','hot','cool',
                              'spring','summer','autumn','winter',
                              'gray','bone','copper','pink',)
        
        self.box.bind("<<ComboboxSelected>>", self.select_cmap)
        self.box.current(0)
        self.box.pack()
    
    def select_cmap(self, event):
        self.map.change_cmap(self.box.get())