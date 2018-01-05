'''
Created on 28 nov. 2017

@author: Josefine
'''
from Tkinter import Label, Entry, Button, IntVar, StringVar
import ttk

class FrameFormat(object):

    def __init__(self,gui, master, frame):
        self.main_label = Label(frame, text = "TIMESAT image viewer")
        self.type_label = Label(frame, text = "Image file type")
        type_box_value = StringVar()
        self.type_box = ttk.Combobox(frame, textvariable=type_box_value, state='readonly')
        self.type_box['values'] = ('8-bit unsigned integer', '16-bit signed integer', '32-bit real',)
        self.type_box.current(0)
        self.order_label = Label(frame, text = "Byte order")
        order_box_value = StringVar()
        self.order_box = ttk.Combobox(frame, textvariable=order_box_value, state='readonly')
        self.order_box['values'] = ('Little endian','Big endian',)
        self.order_box.current(0)
        self.row_label = Label(frame, text = "Nbr of rows")
        self.col_label = Label(frame, text = "Nbr of columns")
   
        self.row_var = IntVar()
        self.col_var = IntVar()
        
        vcmd = master.register(self.nbr_check) # we have to wrap the command
        self.row_entry = Entry(frame, validate="key", validatecommand=(vcmd, '%P'), textvariable = self.row_var)
        self.col_entry = Entry(frame, validate="key", validatecommand=(vcmd, '%P'), textvariable = self.col_var)

        self.draw_button = Button(frame, text="Draw", command=lambda: gui.display(self.type_box.get(), self.order_box.get(), self.row_entry.get(),self.col_entry.get()))
        
        self.main_label.grid(row=0, column=0, sticky='w')
        self.type_label.grid(row=1, column=0, sticky='w')
        self.type_box.grid(row=1,column=1,sticky='e')
        self.order_label.grid(row=2, column=0, sticky='w')
        self.order_box.grid(row=2,column=1,sticky='e')

        self.row_label.grid(row=3, column=0, sticky='w')
        self.row_entry.grid(row=3, column=1, sticky='e')
        self.col_label.grid(row=4, column=0, sticky='w')
        self.col_entry.grid(row=4, column=1, sticky='e')

        self.draw_button.grid(row=4, column=2, sticky='e')
        
    #Only numbers in the entries
    def nbr_check(self, new_text):
        if not new_text:        # the field is being cleared
            return True         # return that the entry is empty
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False
        
    def draw(self):
        # Run when draw button is pressed
        # Update a matrix with the loaded file
        print('Drawing','Row entry', self.row_entry.get(),
              'Column entry', self.col_entry.get())
