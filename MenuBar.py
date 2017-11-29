'''
Created on 28 nov. 2017

@author: Josefine
'''

from Tkinter import Menu
#from menu_commands import *
from image import *


class MenuBar(object):

    def __init__(self, master):
        menu = Menu(master)
        master.config(menu=menu)        
        subMenu = Menu()        
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Open image file", command=open_file)
        subMenu.add_command(label="Open file list", command=file_list)
        subMenu.add_separator()
        subMenu.add_command(label="Printing Window", command=printing_window)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=exit)
        
        editMenu = Menu(menu)
        menu.add_cascade(label ="Help", menu = editMenu)
        editMenu.add_command(label="About", command=about)

def open_file():
    filename = file_dialog()
    print 'Open file: ', filename


def file_list():
    print 'Open file list'


def printing_window():
    print 'Open printing window'


def exit():
    print 'Exit program'


def about():
    print 'About'