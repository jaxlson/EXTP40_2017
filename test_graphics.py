from Tkinter import *
import random

master = Tk()

w = Canvas(master, width=300, height=300)
w.pack()

rows = 10
cols = 10

px = [random.randint(0, 255) for n in range(100)]
x = 0
y = 0
side = 30

def color(n): #om n ar max 255. Ger # foljt av hex
    #print 'n:', n
    if n<16:
        h = '#00'+hex(n)[2:]
    else:
        h = '#0'+hex(n)[2:]
    #print 'h: ', h
    return h

for r in range(rows):
    for c in range(cols):
        w.create_rectangle(x, y, x + side, y + side, fill = color(px[r*rows + c]))
        x = x + side
    y = y + side
    x = 0

mainloop()