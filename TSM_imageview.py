from Tkinter import Tk, Frame, LEFT, BOTH, BOTTOM, Y, X
import matplotlib

matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
from MenuBar import MenuBar
from FrameFormat import FrameFormat
from FrameScale import FrameScale
from FrameView import FrameView
from FrameHist import FrameHist
from CmapBox import CmapBox

class TSM_ImageView:
    # Divide in to MVC model, or just separate classes 
    def __init__(self, master):
 
        master.title("TSM Image View")

        # Create frames for right and left "columns"
        frame_left = Frame(master)
        frame_right = Frame(master)
        
        # Default start pic/array
        a = np.fromfile('wa_cl99122.img', dtype= 'uint8')
        self.file_path = None
        
        # Menu
        MenuBar(self, master)
        
        # Create format frame with widgets
        frame_format = Frame(frame_left)
        # Use self(tsm_imageview) as parameter to call display method
        frameF = FrameFormat(self, master, frame_format)
        
        # Create histogram
        frame_hist = Frame(frame_left)
        frameH = FrameHist(frame_hist, a) 
            
        # Create map frame with widgets
        frame_map=Frame(frame_right)
        self.frameV = FrameView(frame_map,a, frameH, frameF)
        
        # Create scale frame with widgets
        frame_scale = Frame(frame_left)
        self.frameS = FrameScale(a, frame_scale, self.frameV)
        
        # Create combobox for colormap selection
        CmapBox(frame_right, self.frameV)
        
        # Layout - widget positioning
        frame_left.pack(side=LEFT, fill=Y, padx=5, pady=5)
        frame_right.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        frame_format.pack(fill=X, expand=True)
        frame_hist.pack(fill=Y, expand=True, padx=10, pady=20)
        frame_scale.pack(side= BOTTOM, expand=True)
        frame_map.pack(fill=BOTH, expand=True)
    
    # Set f to the new file path, update in display()
    def set_image(self, f):
        self.file_path = f.encode('utf-8')
        print self.file_path  
        
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
        # Bug: all little endian turns to hardware-native
        if im_type[0] == '8':
            im_type = np.dtype('uint8')
        elif im_type[0] == '1' and order[0] == 'L':
            im_type = np.dtype('<i2') 
        elif im_type[0] == '1' and order[0] == 'B':
            im_type = np.dtype('>i2')
        elif im_type[0] == '3' and order[0] == 'L':
            im_type = np.dtype('<f4') 
        elif im_type[0] == '3' and order[0] == 'B':
            im_type = np.dtype('>f4')
        else:
            print "Wrong input"
            return
        if self.file_path != None:
            image_file = np.fromfile(self.file_path, dtype=im_type)
            self.frameV.update_plot(image_file, row, col, self.file_path)
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


