from Tkinter import *
import Tkinter
import tkFileDialog
import random
from compiler.pycodegen import EXCEPT


def file_dialog():
    f = tkFileDialog.askopenfilename()

    if f is not None:
        return f


def read_integers(filename):
    with open(filename) as img:
        img_list = [map(int,x.split()) for x in img if x.strip] #creates a list with one element, which is a list of ints. Don't know why, and it's weird...
        img_list = img_list[0] #takes the list of ints and returns it.
    
    return img_list

master = Tk()

w = Canvas(master, width=1000, height=1000)
w.pack()

rows = 13
cols = 11

#px = [random.randint(0, 255) for n in range(10000)]
#px = read_integers("test2.txt")
px = read_integers(file_dialog())
print 'length: ', len(px), 'px: ', px
x = 0
y = 0
side = 10

def color(n): #om n ar max 255. Ger # foljt av hex
    #print 'n:', n
    if n < 16:
        h = '#00'+hex(n)[2:]
    else:
        h = '#0'+hex(n)[2:]
    #print 'h: ', h
    return h

for r in range(cols):
    for c in range(rows):
        try:
            w.create_rectangle(x, y, x + side, y + side, fill = color(px[r*rows + c]), outline = "")
        except:
            w.create_rectangle(x, y, x + side, y + side, fill = 'magenta', outline = "")
        x = x + side
    y = y + side
    x = 0

mainloop()