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
        subMenu.add_command(label="Open image file", command=self.open_file)
        subMenu.add_command(label="Open file list", command=self.file_list)
        subMenu.add_separator()
        subMenu.add_command(label="Printing Window", command=self.printing_window)
        subMenu.add_separator()
        subMenu.add_command(label="Exit", command=self.exit)
        
        editMenu = Menu(menu)
        menu.add_cascade(label ="Help", menu = editMenu)
        editMenu.add_command(label="About", command=self.about)

    def open_file(self,):
        f = file_dialog()
        print 'Open file: ', f

    def file_list(self):
        print 'Open file list'

    def printing_window(self):
        print 'Open printing window'

    def exit(self):
        print 'Exit program'

    def about(self):
        print 'About'
