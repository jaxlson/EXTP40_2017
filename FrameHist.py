'''
Created on 30 nov. 2017

@author: Josefine
'''
from Tkinter import BOTH,YES
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Hist import Hist
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class FrameHist(object):

    def __init__(self,frame, a):
        f = Figure(figsize=(5,4), dpi=100)
        canvas = FigureCanvasTkAgg(f, frame)
        canvas.get_tk_widget().pack(fill=BOTH, expand=YES)
        
        plt = f.gca()
        plt.hist(a,bins='auto')
        canvas.show()
    
    def change_scale(self):
        self.hist.update()
        
    def update_hist(self):
        return