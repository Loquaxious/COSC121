from tkinter import *
from tkinter.ttk import *

def process_name():
    """Do something with the name (in this case just print it)"""

    global name_entry
    print("Name = " + name_entry.get())

def main():
    """Set up the GUI and run it"""

    global name_entry
    window = Tk()
    name_label = Label(window, text='Enter name:')
    name_label.grid(row=0, column=0)
    name_entry = Entry(window)
    name_entry.grid(row=0, column=1)
    button = Button(window, text='Go', command=process_name, padding=10)
    button.grid(row=1, column=0, columnspan=2)
    window.mainloop()

main()