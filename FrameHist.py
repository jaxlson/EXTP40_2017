'''
Created on 30 nov. 2017

@author: Josefine
'''
from Tkinter import BOTH,YES
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Hist import Hist

class FrameHist(object):

    def __init__(self,frame, a):
        self.hist = Hist(a)
        raster_hist = self.hist.figure()
        canvas_hist = FigureCanvasTkAgg(raster_hist,frame)
        canvas_hist.show()
        canvas_hist.get_tk_widget().pack(fill=BOTH, expand=YES)
        canvas_hist._tkcanvas.pack()
    
    def change_scale(self):
        self.hist.update()     