from tkinter import *
from tkinter.ttk import *

def process_name():
    """Do something with the name"""

    global name_entry, hello_label
    template = "Hi " + name_entry.get()
    hello_label['text'] = template 


def main():
    """Set up the GUI and run it"""
    
    global name_entry, hello_label
    window = Tk()
    
    name_label = Label(window, text="Enter a name below")
    name_label.grid(row=0, column=0)
    
    name_entry = Entry(window)
    name_entry.grid(row=1, column=0)
    
    button = Button(window, text='Say hello', command=process_name)
    button.grid(row=2, column=0)
    
    hello_label = Label(window, text="")
    hello_label.grid(row=3, column= 0)
    
    window.mainloop()

main()
    