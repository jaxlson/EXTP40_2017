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


class TSM_ImageView:
    # Divide in to MVC model, or just separate classes 
    def __init__(self, master):
        self.master = master
        self.combo(master)
        master.title("TSM Image View")
        
        # Menu
        MenuBar(master)
        
        # Create format frame with widgets
        self.frame_format = Frame(master)
        FrameFormat(master, self.frame_format)

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

        self.frame = Frame(master) 
        canvas = FigureCanvasTkAgg(f, self.frame)
        canvas.show()
        canvas.get_tk_widget().pack()

        toolbar = NavigationToolbar2TkAgg(canvas, self.frame)
        toolbar.update()
        canvas._tkcanvas.pack()

        # Layout - widget positioning
        self.frame_format.grid(row=0, column=0, sticky=N)        

        #self.img_frame.grid(row=0, column=2)
        self.frame.grid(row=0, column =2)
        

    def combo(self, master):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.master, textvariable=self.box_value, 
                                state='readonly')
        self.box['values'] = ('A', 'B', 'C')
        self.box.current(0)
        self.box.grid(column=2, row=1)
    
    def on_closing(self):
            # messegebox asking for exits
            plt.close()
            root.destroy()  

root = Tk() 
my_gui = TSM_ImageView(root)
root.protocol("WM_DELETE_WINDOW", my_gui.on_closing)
root.mainloop()


