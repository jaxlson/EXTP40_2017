from Tkinter import Tk, Frame, LEFT, BOTH, BOTTOM, Y, Text
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
        
        # Default start pic/array
        a = np.fromfile('wa_cl99122.img', dtype= 'uint8')
        self.file_path = None
        
        # Menu
        MenuBar(self, master)
        
        # Create format frame with widgets
        self.frame_format = Frame(self.frame_left)
        # Use self(tsm_imageview) as parameter to call display method
        FrameFormat(self, master, self.frame_format)
        
        # Create histogram
        self.frame_hist = Frame(self.frame_left)
        FrameHist(self.frame_hist, a) 
            
        # Create map frame with widgets
        self.frame_map=Frame(self.frame_right)
        self.frameV = FrameView(self.frame_map,a)
        
        # Create scale frame with widgets
        self.frame_scale = Frame(self.frame_left)
        FrameScale(a, self.frame_scale, self.frameV)
        
        # Create combobox for colormap selection
        ComboBox(self.frame_right, self.frameV)
        
        # Layout - widget positioning
        self.frame_left.pack(side=LEFT, fill=Y, padx=5, pady=5)
        self.frame_right.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        self.frame_format.pack(expand=True)
        self.frame_hist.pack(fill=Y, expand=True, padx=10, pady=20)
        self.frame_scale.pack(side= BOTTOM, expand=True)
        self.frame_map.pack(fill=BOTH, expand=True)
    
    # Set a to the new file path, update in display()
    def set_image(self, f):
        self.file_path = f.encode('utf-8')  
        
    # Displays the loaded image
    # Parameters from FrameFormat: image file type, byte order, Nbr of rows, Nbr of col
    # TO-DO Error messages displayed in the gui
    
    def display(self, im_type, order, row, col):
        row = int(row)
        col = int(col)
        
        # Check input data
        if row == 0 or col == 0:
            print "Rows or Columns can not be 0, enter a correct number"
            return
        
        # image type and order -> dtype
        if im_type[0] == '8':
            im_type = 'uint8'
        elif im_type[0] == '1' and order[0] == 'L':
            im_type = '<iint16'
        elif im_type[0] == '1' and order[0] == 'B':
            im_type = '>iint16'
        elif im_type[0] == '3' and order[0] == 'L':
            im_type = '<float32'  
        elif im_type[0] == '3' and order[0] == 'B':
            im_type = '>float32'
        else:
            print "Wrong input"
            return
        if self.file_path != None:
            image_file = np.fromfile(self.file_path, dtype=im_type)
            self.frameV.update_plot(image_file, row, col)
        else:
            print "No image loaded"
        
    # Closing window and plots            
    def on_closing(self):
            # TO-DO messegebox asking for exits
            plt.close('all')
            root.destroy()  
    
root = Tk() 
my_gui = TSM_ImageView(root)
root.protocol("WM_DELETE_WINDOW", my_gui.on_closing)
root.mainloop()


