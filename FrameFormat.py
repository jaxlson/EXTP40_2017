'''
Created on 28 nov. 2017

@author: Josefine
'''
from Tkinter import Label, Entry, Button

class FrameFormat(object):


    def __init__(self, master, frame):
        self.main_label =  Label(frame, text = "TIMESAT image viewer")
        self.type_label = Label(frame, text = "Image file type")
        self.order_label = Label(frame, text = "Byte order")
        self.row_label = Label(frame, text = "Nbr of rows")
        self.col_label = Label(frame, text = "Nbr of columns")

        vcmd = master.register(self.nbr_check) # we have to wrap the command
        self.row_entry = Entry(frame, validate="key", validatecommand=(vcmd, '%P'))
        self.col_entry = Entry(frame, validate="key", validatecommand=(vcmd, '%P'))

        self.draw_button = Button(frame, text="Draw", command=lambda: self.draw())
        
        self.main_label.grid(row=0, column=0)
        self.type_label.grid(row=1, column=0)
        self.order_label.grid(row=2, column=0)

        self.row_label.grid(row=3, column=0)
        self.row_entry.grid(row=3, column=1)
        self.col_label.grid(row=4, column=0)
        self.col_entry.grid(row=4, column=1)

        self.draw_button.grid(row=4, column=2)
    
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