from tkinter import *
from tkinter.ttk import *

def main():
    """Create a hollo world lable"""
    window = Tk()
    hello_label = Label(window, text='Hello World!')
    hello_label.grid(row=0, column=0)
    window.mainloop()
    
main()
    