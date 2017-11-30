'''
Created on 30 nov. 2017

@author: Josefine
'''
import numpy as np
import pylab as plt
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from Tkinter import *

class FrameView(object):


    def __init__(self, frame, a):
        # Reshape to the right rows and cols
        a = a.reshape(200,200)

        # Display the image
        im = plt.imshow(a, cmap= 'brg')
        plt.colorbar(im, orientation = 'vertical')
        f = plt.gcf() 
        canvas_map = FigureCanvasTkAgg(f, frame)
        canvas_map.show()
        canvas_map.get_tk_widget().pack()
        toolbar = NavigationToolbar2TkAgg(canvas_map, frame)
        toolbar.update()
        canvas_map._tkcanvas.pack(fill=BOTH, expand=TRUE)
    
    def get_array(self):
        return self.a   