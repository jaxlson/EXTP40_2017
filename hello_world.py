
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
    
if __name__ == '__main__':
    main()