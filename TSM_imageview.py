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


class TSM_ImageView:
    # Divide in to MVC model, or just separate classes 
    def __init__(self, master):
        self.master = master
        self.combo()
        master.title("TSM Image View")
        
        # Menu
        MenuBar(master)
        
        # Create format frame with widgets
        self.frame_format = Frame(master)
        frameF = FrameFormat(master, self.frame_format)
        # get entry value frameF.col_entry.get() 
        
        # Load an image file
        a = np.fromfile('wa_cl00011.img', dtype=np.uint8)

        # Reshape to the right rows and cols
        a = a.reshape(200,200)

        # Display the image
        # cmaps: jet, parula, hsv, hot, cool, spring, summer, autumn, winter
        #        grey, bone, copper, pink, colorcube,  
        im = plt.imshow(a, cmap= 'brg')
        plt.colorbar(im, orientation = 'vertical')
        f = plt.gcf()

        self.frame_map = Frame(master) 
        canvas_map = FigureCanvasTkAgg(f, self.frame_map)
        canvas_map.show()
        canvas_map.get_tk_widget().pack()

        toolbar = NavigationToolbar2TkAgg(canvas_map, self.frame_map)
        toolbar.update()
        canvas_map._tkcanvas.pack(fill=BOTH, expand=TRUE)
        
        # Display Histogram
        hist = Hist(a)
        raster_hist = hist.figure()
        
        self.frame_hist = Frame(master) 
        canvas_hist = FigureCanvasTkAgg(raster_hist, self.frame_hist)
        canvas_hist.show()
        canvas_hist.get_tk_widget().pack()

        # toolbar = NavigationToolbar2TkAgg(canvas_hist, self.frame)
        # toolbar.update()
        canvas_hist._tkcanvas.pack()
        
        # Layout - widget positioning
        self.frame_format.pack(side=LEFT, fill=BOTH)        

        self.frame_map.pack(fill=BOTH, expand=TRUE)
        
        self.frame_hist.pack()
        
    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.master, textvariable=self.box_value, 
                                state='readonly')
        self.box['values'] = ('A', 'B', 'C')
        self.box.current(0)
        self.box.pack(side=BOTTOM)
    
    def on_closing(self):
            # messegebox asking for exits
            plt.close('all')
            root.destroy()  

root = Tk() 
my_gui = TSM_ImageView(root)
root.protocol("WM_DELETE_WINDOW", my_gui.on_closing)
root.mainloop()


