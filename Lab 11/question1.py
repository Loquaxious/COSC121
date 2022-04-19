"""Display a windowing saying 'COSC121'"""
from tkinter import *
from tkinter.ttk import *

def main():
    """Construct the GUI and start it running"""
    window = Tk()
    cosc_label = Label(window, text='COSC is Great')
    cosc_label.grid(row=0, column=0)
    window.mainloop()

main()