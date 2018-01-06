'''
Created on 30 nov. 2017

@author: Josefine
'''
import numpy as np
import pylab as plt
import matplotlib
from numpy import shape

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from Tkinter import BOTH, TRUE

class FrameView(object):
    
    def __init__(self, frame, img_array):
        # Reshape to the right rows and cols
        # Values from frameformat
        img_array = img_array.reshape(200,200)

        # Display the image
        self.im = plt.imshow(img_array, cmap= 'brg')
        plt.colorbar(self.im, orientation = 'vertical')
        self.f = plt.gcf() 
        self.canvas_map = FigureCanvasTkAgg(self.f, frame)
        self.canvas_map.show()
        self.canvas_map.get_tk_widget().pack()
        toolbar = NavigationToolbar2TkAgg(self.canvas_map, frame)
        toolbar.update()
        self.canvas_map._tkcanvas.pack(fill=BOTH, expand=TRUE)
        
    def change_cmap(self, colormap):
        self.im.set_cmap(colormap)
        self.canvas_map.draw()
    
    def change_clim(self, vmin, vmax):
        self.im.set_clim(vmin,vmax)
        self.canvas_map.draw()
    
    def update_plot(self, a, row, col):
        # TO-DO display error in gui
        try:
            a = a.reshape((row,col))
        except TypeError as te:
            print te
            return
        except ValueError as ve:
            print ve
            return
        
        self.im.set_data(a)
        self.canvas_map.draw()