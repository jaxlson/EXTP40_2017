
import Tkinter
from Tkinter import tkinter
import tkMessageBox
from Tkconstants import COMMAND

def main():
    print "Start TKinter window"
    # Open a small window
    top = Tkinter.Tk()
    
    def helloCallBack():
        tkMessageBox.showinfo("Hello Python", "Hello World")
        
    B = Tkinter.Button(top, text = "Hello", command = helloCallBack)
    
    B.pack()    
    top.mainloop()
    
    # create an image array based on the file and input number of rows and col
    # find min and max in the image array
    # numpy array, matplotlib imshow or glumpy
    # change the color scale
    
if __name__ == '__main__':
    main()
