from Tkinter import Tk, Frame, LEFT, BOTH, YES, Y 
import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import pylab as plt
from MenuBar import MenuBar
from FrameFormat import FrameFormat
from FrameScale import FrameScale
from FrameView import FrameView
from FrameHist import FrameHist
from ComboBox import ComboBox

class TSM_ImageView:
    # Divide in to MVC model, or just separate classes 
    def __init__(self, master):
 
        master.title("TSM Image View")

        # Create frames for right and left "columns"
        self.frame_left = Frame(master)
        self.frame_right = Frame(master)

        filename = 'default'
        a = np.fromfile('wa_cl00011.img', dtype=np.uint8)
        
        # Menu
        MenuBar(master)
        
        # Create format frame with widgets
        self.frame_format = Frame(self.frame_left)
        frameF = FrameFormat(master, self.frame_format)
            # get entry value frameF.col_entry.get()
        
        # Create histogram
        self.frame_hist = Frame(self.frame_left)
        frameH = FrameHist(self.frame_hist, a) 
                
        # Create scale frame with widgets
        self.frame_scale = Frame(self.frame_left)
        frameS = FrameScale(a, self.frame_scale)
            
        # Create map frame with widgets
        self.frame_map=Frame(self.frame_right)
        frameV = FrameView(self.frame_map,a)
        
        # Create combobox for colormap selection
        combo = ComboBox(self.frame_right, frameV)
        
        # Layout - widget positioning
        self.frame_left.pack(side=LEFT, fill=Y, padx=5, pady=5)
        self.frame_right.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        self.frame_format.pack(fill=Y, expand=True)
        self.frame_hist.pack(fill=Y, expand=True)
        self.frame_scale.pack(fill=Y,expand=True)
        self.frame_map.pack(fill=BOTH, expand=True)
    
    # Closing window and plots            
    def on_closing(self):
            # messegebox asking for exits
            plt.close('all')
            root.destroy()  

root = Tk() 
my_gui = TSM_ImageView(root)
root.protocol("WM_DELETE_WINDOW", my_gui.on_closing)
root.mainloop()


