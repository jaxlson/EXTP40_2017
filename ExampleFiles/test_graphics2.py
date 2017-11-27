'''
Created on 24 nov. 2017

@author: Josefine
'''
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import pylab as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()
root.wm_title("Embedding in TK")

# Load an image file
a = np.fromfile('wa_cl00011.img', dtype=np.uint8)
# Reshape to the right rows and cols
a = a.reshape(200,200)
# Display the image
im = plt.imshow(a, cmap= 'hot')
plt.colorbar(im, orientation = 'vertical')
f = plt.gcf()
 
canvas = FigureCanvasTkAgg(f, master=root)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)


def on_key_event(event):
    print('you pressed %s' % event.key)
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect('key_press_event', on_key_event)


def _quit():
    root.quit()     
    root.destroy()  

button = Tk.Button(master=root, text='Quit', command=_quit)
button.pack(side=Tk.LEFT)

Tk.mainloop()
