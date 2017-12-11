'''
Created on 28 nov. 2017

@author: Josefine
'''
from Tkinter import Label, Entry, Scale, HORIZONTAL, IntVar, END
import numpy as np

class FrameScale(object):
 
    def __init__(self, a, frame, view):
        self.view = view
        # Image min and max values        
        self.min_var = IntVar(value=np.amin(a))
        self.max_var = IntVar(value=np.amax(a))
        
        self.min_label = Label(frame, text = "Min.")
        self.max_label = Label(frame, text = "Max.")
        
        self.min_entry = Entry(frame, textvariable=self.min_var)
        self.max_entry = Entry(frame, textvariable=self.max_var)
        
        self.min_entry.bind("<Return>", lambda event: min_entry_change(self.min_scale,self.min_var.get()))
        self.max_entry.bind("<Return>", lambda event: max_entry_change(self.max_scale,self.max_var.get()))
        
        def min_change(val):
            val = int(val)
            temp = self.max_var.get()
            if(val < temp):
                self.min_var.set(val)
                self.view.change_clim(val,temp)
            else:
                self.min_var.set(temp-1)
                self.view.change_clim(temp-1,temp)
        
        def max_change(val):
            val = int(val)
            temp = self.min_var.get()
            if(val > temp):
                self.max_var.set(val)
                self.view.change_clim(temp,val)
            else:
                self.min_var.set(temp+1)
                self.view.change_clim(temp,temp+1)
        
        self.min_scale = Scale(frame, orient=HORIZONTAL, from_=np.amin(a), to=np.amax(a)-1, command=min_change)
        self.max_scale = Scale(frame, orient=HORIZONTAL, from_=np.amin(a)+1, to=np.amax(a), command=max_change)
        
        self.min_scale.set(np.amin(a))
        self.max_scale.set(np.amax(a))
               
        self.min_label.grid(row=0, column=0, sticky='w')
        self.max_label.grid(row=1, column=0, sticky='w')
        self.min_entry.grid(row=0, column=1)
        self.max_entry.grid(row=1, column=1)
        self.min_scale.grid(row=0, column=2, sticky='e')
        self.max_scale.grid(row=1, column=2, sticky='e')
        
        def min_entry_change(scale, value):
            if(value < int(self.max_var.get())):
                scale.configure(from_=value-20, to=value+20)
                scale.set(value)
            else:
                scale.configure(from_=value-20, to=value+20)
                scale.set(int(self.max_var.get())-1)
        
        def max_entry_change(scale, value):
            if(value > int(self.min_var.get())):
                scale.configure(from_=value-20, to=value+20)
                scale.set(value)
            else:
                scale.configure(from_=value-20, to=value+20)
                scale.set(int(self.min_var.get())+1)
            