from Tkinter import *
import Tkinter
import tkFileDialog
import random
from compiler.pycodegen import EXCEPT


def file_dialog():
    #root = Tkinter.Tk()
    f = tkFileDialog.askopenfilename()

    if f is not None:
        return f


def read_integers(filename):
    with open(filename) as img:
        img_list = [map(int, x.split()) for x in img if
                    x.strip]  # creates a list with one element, which is a list of ints. Don't know why, and it's weird...
        img_list = img_list[0]  # takes the list of ints and returns it.
        print img_list

    return img_list


master = Tk()

w = Canvas(master, width=1000, height=1000)
w.pack()

file_dialog()

mainloop()