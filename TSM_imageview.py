from Tkinter import Tk, Frame, LEFT, BOTH, BOTTOM, Y, Text
import matplotlib
import matplotlib.image as mpimg
from matplotlib.cbook import Null
from numpy import dtype

matplotlib.use('TkAgg')
import numpy as np
import pylab as plt
from MenuBar import MenuBar
from FrameFormat import FrameFormat
from FrameScale import FrameScale
from FrameView import FrameView
from FrameHist import FrameHist
from ComboBox import ComboBox
from FilePathText import FilePathText

class TSM_ImageView:
    # Divide in to MVC model, or just separate classes 
    def __init__(self, master):
 
        master.title("TSM Image View")

        # Create frames for right and left "columns"
        self.frame_left = Frame(master)
        self.frame_right = Frame(master)
        
        # Default start pic/array
        # global a
        # a = np.zeros((50,50))
        a = np.fromfile('wa_cl99122.img', dtype= 'uint8')
        
        self.loaded_image_file = Null
        
        # Menu
        MenuBar(self, master)
        
        # Create format frame with widgets
        self.frame_format = Frame(self.frame_left)
        # Use self(tsm_imageview) as parameter to call display method
        frameF = FrameFormat(self, master, self.frame_format)
        
        # Create histogram
        self.frame_hist = Frame(self.frame_left)
        frameH = FrameHist(self.frame_hist, a) 
            
        # Create map frame with widgets
        self.frame_map=Frame(self.frame_right)
        self.frameV = FrameView(self.frame_map,a)
        
        # Create scale frame with widgets
        self.frame_scale = Frame(self.frame_left)
        frameS = FrameScale(a, self.frame_scale, self.frameV)
        
        # Create combobox for colormap selection
        combo = ComboBox(self.frame_right, self.frameV)

        # Write the file path
        FilePathText(master)
        
        # Layout - widget positioning
        self.frame_left.pack(side=LEFT, fill=Y, padx=5, pady=5)
        self.frame_right.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        self.frame_format.pack(expand=True)
        self.frame_hist.pack(fill=Y, expand=True, padx=10, pady=20)
        self.frame_scale.pack(side= BOTTOM, expand=True)
        self.frame_map.pack(fill=BOTH, expand=True)
    
    def set_image(self, f):
        # set a to the new file, update in display()
        # this does not work
        f = f.encode('utf-8')
        self.loaded_image_file = np.fromfile(f, dtype=np.uint8)
        print f, type(f)
        
        
    # Displays the loaded image
    # Parameters from FrameFormat: image file type, byte order, Nbr of rows, Nbr of col
    def display(self, im_type, order, row, col):
        print "drawing", im_type, order, row, col
        self.frameV.update_plot(self.loaded_image_file)
    
    # Closing window and plots            
    def on_closing(self):
            # messegebox asking for exits
            plt.close('all')
            root.destroy()  
    
root = Tk() 
my_gui = TSM_ImageView(root)
root.protocol("WM_DELETE_WINDOW", my_gui.on_closing)
root.mainloop()


