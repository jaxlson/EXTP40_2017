'''
Created on 30 nov. 2017

@author: Josefine
'''
import pylab as plt
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from Tkinter import BOTH, TRUE

class FrameView(object):
    
    def __init__(self, frame, img_array):
        img_array = img_array.reshape(200,200) #The rows and cols of the default image

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
        # TODO: display error in gui
        img_a = a.reshape((row,col))
        self.im.set_data(img_a)
        self.canvas_map.draw()