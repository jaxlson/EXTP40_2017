from Tkinter import *
from PIL import ImageTk, Image


class TSM_ImageView:
    # Divide in to MVC model, or just separate classes 
    def __init__(self, master):
        self.master = master
        master.title("TSM Image View")
        # Create frames for eg. Format area and Image scaling
        # Use pack in frames and grid to place frames and objects
        # Widgets
        self.main_label =  Label(master, text = "TIMESAT image viewer")
        self.type_label = Label(master, text = "Image file type")
        self.order_label = Label(master, text = "Byte order")
        self.row_label = Label(master, text = "Nbr of rows")
        self.col_label = Label(master, text = "Nbr of columns")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.row_entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.col_entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.draw_button = Button(master, text="Draw", command=lambda: self.draw())

        path = "py.png"
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.img_frame = Label(master, image = self.img)

        # Layout - widget positioning
        self.main_label.grid(row=0, column=0, sticky=W)
        self.type_label.grid(row=1, column=0, sticky=W)
        self.order_label.grid(row=2, column=0, sticky=W)

        self.row_label.grid(row=3, column=0, sticky=W)
        self.row_entry.grid(row=3, column=1, sticky=E)
        self.col_label.grid(row=4, column=0, sticky=W)
        self.col_entry.grid(row=4, column=1, sticky=E)

        self.draw_button.grid(row=4, column=2)

        self.img_frame.grid(row=0, column=2)
        
        
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

root = Tk()
my_gui = TSM_ImageView(root)
root.mainloop()
