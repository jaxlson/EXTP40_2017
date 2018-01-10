'''
Created on 28 nov. 2017

@author: Josefine
'''

from Tkinter import Menu
import tkFileDialog

class MenuBar(object):

    def __init__(self, gui, master):
        self.gui = gui
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

    def open_file(self):
        f = tkFileDialog.askopenfilename()       
        self.gui.set_image(f)

    #TODO: Add proper functionality
    def file_list(self):
        print 'Open file list'

    #TODO: Add proper functionality
    def printing_window(self):
        print 'Open printing window'

    def exit(self):
        self.gui.on_closing()

    #TODO: Add proper functionality
    def about(self):
        print 'About'
