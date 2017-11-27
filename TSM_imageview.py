from Tkinter import *
from PIL import ImageTk, Image
import matplotlib
import ttk

matplotlib.use('TkAgg')

import numpy as np
import pylab as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler


class TSM_ImageView:
    # Divide in to MVC model, or just separate classes 
    def __init__(self, master):
        self.master = master
        self.combo(master)
        master.title("TSM Image View")
        # Create frames for eg. Format area and Image scaling
        # Use pack in frames and grid to place frames and objects
        # Widgets
        self.frame_left = Frame(master)
        self.main_label =  Label(self.frame_left, text = "TIMESAT image viewer")
        self.type_label = Label(self.frame_left, text = "Image file type")
        self.order_label = Label(self.frame_left, text = "Byte order")
        self.row_label = Label(self.frame_left, text = "Nbr of rows")
        self.col_label = Label(self.frame_left, text = "Nbr of columns")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.row_entry = Entry(self.frame_left, validate="key", validatecommand=(vcmd, '%P'))
        self.col_entry = Entry(self.frame_left, validate="key", validatecommand=(vcmd, '%P'))

        self.draw_button = Button(self.frame_left, text="Draw", command=lambda: self.draw())

        #path = "py.png"
        #self.img = ImageTk.PhotoImage(Image.open(path))
        #self.img_frame = Label(master, image = self.img)

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
        self.frame_left.grid(row=0, column=0, sticky=N)
        self.main_label.grid(row=0, column=0, sticky=W)
        self.type_label.grid(row=1, column=0, sticky=W)
        self.order_label.grid(row=2, column=0, sticky=W)

        self.row_label.grid(row=3, column=0, sticky=W)
        self.row_entry.grid(row=3, column=1, sticky=E)
        self.col_label.grid(row=4, column=0, sticky=W)
        self.col_entry.grid(row=4, column=1, sticky=E)

        self.draw_button.grid(row=4, column=2)

        #self.img_frame.grid(row=0, column=2)
        self.frame.grid(row=0, column =2)
        
        
    def validate(self, new_text):
        if not new_text: # the field is being cleared
            #return that the entry is empty
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def draw(self):
        # Run when draw button is pressed
        # Update a matrix with the loaded file
        print("Drawing")

    def combo(self, master):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.master, textvariable=self.box_value, 
                                state='readonly')
        self.box['values'] = ('A', 'B', 'C')
        self.box.current(0)
        self.box.grid(column=2, row=1)
        

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu()

menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Open image file")
subMenu.add_command(label="Open file list")
subMenu.add_separator()
subMenu.add_command(label="Printing Window")
subMenu.add_separator()
subMenu.add_command(label="Exit", command = root.quit())

editMenu = Menu(menu)
menu.add_cascade(label ="Help", menu = editMenu)
editMenu.add_command(label="About")

my_gui = TSM_ImageView(root)
root.mainloop()
