'''
Created on 28 nov. 2017

@author: Elisabeth
'''
import tkFileDialog

#nagonstans borde vi testa att filen faktiskt ar av ratt typ

def file_dialog():
    filename = tkFileDialog.askopenfilename()

    if filename is not None:
        return filename


def read_integers(filename):
    with open(filename) as img:
        img_list = [map(int,x.split()) for x in img if x.strip] #creates a list with one element, which is a list of ints. Don't know why, and it's weird...
        img_list = img_list[0] #takes the list of ints and returns it.
    
    return img_list

