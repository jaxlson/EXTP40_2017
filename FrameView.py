'''
Created on 30 nov. 2017

@author: Josefine
'''
import numpy as np
import pylab as plt
import matplotlib

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
    
    def update_plot(self):
        # this works, need to get open image to update a (array)
        z = np.zeros((50,50))
        self.im.set_data(z)
        self.canvas_map.draw()