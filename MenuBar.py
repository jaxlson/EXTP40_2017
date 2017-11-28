'''
Created on 28 nov. 2017

@author: Josefine
'''

from Tkinter import Menu

class MenuBar(object):

    def __init__(self, master):
        menu = Menu(master)
        master.config(menu=menu)        
        subMenu = Menu()        
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Open image file")
        subMenu.add_command(label="Open file list")
        subMenu.add_separator()
        subMenu.add_command(label="Printing Window")
        subMenu.add_separator()
        subMenu.add_command(label="Exit")
        
        editMenu = Menu(menu)
        menu.add_cascade(label ="Help", menu = editMenu)
        editMenu.add_command(label="About")
        