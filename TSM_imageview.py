from Tkinter import *
import matplotlib
import ttk

matplotlib.use('TkAgg')
import numpy as np
import pylab as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from MenuBar import MenuBar
from FrameFormat import FrameFormat
from Hist import Hist
from FrameScale import FrameScale


class TSM_ImageView:
    # Divide in to MVC model, or just separate classes 
    def __init__(self, master):
 
        master.title("TSM Image View")

        # Create frames for right and left "columns"
        self.frame_left = Frame(master, width=200)
        self.frame_right = Frame(master)

        filename = 'default'
        # Menu
        MenuBar(master)
        
        # Create format frame with widgets
        self.frame_format = Frame(self.frame_left)
        frameF = FrameFormat(master, self.frame_format)
        # get entry value frameF.col_entry.get() 
        
        # Load an image file
        a = np.fromfile('wa_cl00011.img', dtype=np.uint8)
        
        # Create format frame with widgets
        self.frame_scale = Frame(self.frame_left)
        frameS = FrameScale(a, self.frame_scale)
        
        # Reshape to the right rows and cols
        a = a.reshape(200,200)

        # Display the image
        im = plt.imshow(a, cmap= 'brg')
        plt.colorbar(im, orientation = 'vertical')
        f = plt.gcf()
        self.frame_map = Frame(self.frame_right) 
        canvas_map = FigureCanvasTkAgg(f, self.frame_map)
        canvas_map.show()
        canvas_map.get_tk_widget().pack()
        toolbar = NavigationToolbar2TkAgg(canvas_map, self.frame_map)
        toolbar.update()
        canvas_map._tkcanvas.pack(fill=BOTH, expand=TRUE)
        
        # Display Histogram
        hist = Hist(a)
        raster_hist = hist.figure()
        self.frame_hist = Frame(self.frame_left) 
        canvas_hist = FigureCanvasTkAgg(raster_hist, self.frame_hist)
        canvas_hist.show()
        canvas_hist.get_tk_widget().pack(fill=BOTH, expand=YES)
        canvas_hist._tkcanvas.pack()
        
        self.combo(self.frame_right)
        
        # Layout - widget positioning
        self.frame_left.pack(side=LEFT, fill=BOTH, expand=YES, padx=5, pady=5)
        self.frame_right.pack(side=LEFT, fill=BOTH, expand=YES, padx=5, pady=5)
        
        self.frame_format.pack()
        self.frame_hist.pack()
        self.frame_scale.pack()
        self.frame_map.pack()
        
    def combo(self, frame):
        # cmaps: jet, parula, hsv, hot, cool, spring, summer, autumn, winter
        #        grey, bone, copper, pink, colorcube,  
        self.box_value = StringVar()
        self.box = ttk.Combobox(frame, textvariable=self.box_value, 
                                state='readonly')
        self.box['values'] = ('A', 'B', 'C')
        self.box.current(0)
        self.box.pack()
    
    def on_closing(self):
            # messegebox asking for exits
            plt.close('all')
            root.destroy()  

root = Tk() 
my_gui = TSM_ImageView(root)
root.protocol("WM_DELETE_WINDOW", my_gui.on_closing)
root.mainloop()


