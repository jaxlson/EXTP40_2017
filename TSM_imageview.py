from Tkinter import *
import matplotlib
import ttk

matplotlib.use('TkAgg')
import numpy as np
import pylab as plt
from matplotlib.backend_bases import key_press_handler
from MenuBar import MenuBar
from FrameFormat import FrameFormat
from FrameScale import FrameScale
from FrameView import FrameView
from FrameHist import FrameHist


class TSM_ImageView:
    # Divide in to MVC model, or just separate classes 
    def __init__(self, master):
 
        master.title("TSM Image View")

        # Create frames for right and left "columns"
        self.frame_left = Frame(master, width=200)
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
        
        # Create combobox for colormap selection
        box_value = StringVar()
        self.box = ttk.Combobox(self.frame_right, textvariable=box_value, state='readonly')
        self.box['values'] = ('jet', 'parula', 'hsv','hot','cool',
                              'spring','summer','autumn','winter',
                              'grey','bone','copper','pink','colorcube')
        
        self.box.bind("<<ComboboxSelected>>", self.select_cmap)
        self.box.current(0)
        self.box.pack()
        
        # Create map frame with widgets
        self.frame_map=Frame(self.frame_right)
        frameV = FrameView(self.frame_map,a)
        
        # Layout - widget positioning
        self.frame_left.pack(side=LEFT, fill=BOTH, expand=YES, padx=5, pady=5)
        self.frame_right.pack(side=LEFT, fill=BOTH, expand=YES, padx=5, pady=5)
        
        self.frame_format.pack()
        self.frame_hist.pack()
        self.frame_scale.pack()
        self.frame_map.pack()
    
    def select_cmap(self, event):
            print(self.box.get())
            
    def on_closing(self):
            # messegebox asking for exits
            plt.close('all')
            root.destroy()  

root = Tk() 
my_gui = TSM_ImageView(root)
root.protocol("WM_DELETE_WINDOW", my_gui.on_closing)
root.mainloop()


