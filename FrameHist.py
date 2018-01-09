'''
Created on 30 nov. 2017

@author: Josefine
'''
from Tkinter import BOTH,YES
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class FrameHist(object):

    def __init__(self,frame, a):
        self.a = a
        f = Figure(figsize=(5,4), dpi=100)
        self.canvas = FigureCanvasTkAgg(f, frame)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=YES)
        
        self.ax = f.gca()
        self.ax.hist(self.a,bins='auto')
        self.canvas.show()
    
    def change_scale(self):
        self.hist.update()
        
    def update_hist(self, a):
        self.a = a
        self.ax.clear()
        self.ax.hist(self.a,bins='auto')
        self.canvas.draw()