'''
Created on 28 nov. 2017

@author: Josefine
'''
from Tkinter import Label, Entry, Scale, HORIZONTAL, IntVar
import numpy as np

class FrameScale(object):
    # TO-DO Bugs: When the scale bar is dragged to overlap the other the values does not update correctly
    # TO-DO The histogram should be updated when scale is changed
    def __init__(self, a, frame, view):
        self.view = view
        amin = np.amin(a)
        amax = np.amax(a)
        
        # Image min and max values        
        self.min_var = IntVar(value=amin)
        self.max_var = IntVar(value=amax)
        
        self.min_label = Label(frame, text = "Min.")
        self.max_label = Label(frame, text = "Max.")
        
        self.min_entry = Entry(frame, textvariable=self.min_var)
        self.max_entry = Entry(frame, textvariable=self.max_var)
        
        self.min_entry.bind("<Return>", lambda event: self.min_entry_change(self.min_scale,self.min_var.get()))
        self.max_entry.bind("<Return>", lambda event: self.max_entry_change(self.max_scale,self.max_var.get()))
        
        self.min_scale = Scale(frame, orient=HORIZONTAL, from_=amin, to=amax-1, length=150, command= self.min_change)
        self.max_scale = Scale(frame, orient=HORIZONTAL, from_=amin+1, to=amax, length=150, command= self.max_change)
        
        self.min_scale.set(amin)
        self.max_scale.set(amax)
               
        self.min_label.grid(row=0, column=0, sticky='w')
        self.max_label.grid(row=1, column=0, sticky='w')
        self.min_entry.grid(row=0, column=1, ipady=2)
        self.max_entry.grid(row=1, column=1, ipady=2)
        self.min_scale.grid(row=0, column=2, sticky='e', padx=10)
        self.max_scale.grid(row=1, column=2, sticky='e', padx=10)
    
    def min_change(self, val):
            val = int(val)
            temp = self.max_var.get()
            if(val < temp):
                self.min_var.set(val)
                self.view.change_clim(val,temp)
            else:
                self.min_var.set(temp-1)
                self.view.change_clim(temp-1,temp)
        
    def max_change(self,val):
            val = int(val)
            temp = self.min_var.get()
            if(val > temp):
                self.max_var.set(val)
                self.view.change_clim(temp,val)
            else:
                self.min_var.set(temp+1)
                self.view.change_clim(temp,temp+1)    
    
    def min_entry_change(self,scale, value):
        if(value < int(self.max_var.get())):
            scale.configure(from_=value-20, to=value+20)
            scale.set(value)
        else:
            scale.configure(from_=value-20, to=value+20)
            scale.set(int(self.max_var.get())-1)
        
    def max_entry_change(self,  scale, value):
        if(value > int(self.min_var.get())):
            scale.configure(from_=value-20, to=value+20)
            scale.set(value)
        else:
            scale.configure(from_=value-20, to=value+20)
            scale.set(int(self.min_var.get())+1)
                
    def update_limit(self, a):
        self.min_change(np.amin(a))
        self.max_change(np.amax(a))
        self.min_entry_change(self.min_scale, np.amin(a))
        self.max_entry_change(self.max_scale, np.amax(a))
        