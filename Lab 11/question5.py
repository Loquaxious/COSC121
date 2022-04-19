from tkinter import *
from tkinter.ttk import *

def change_value(change):
    """ hello """
    global message_label, value
    value += change
    value_label['text'] = value
    
def subtract_five():
    """subtracts 5 off of value"""
    change_value(-5)
    
def subtract_one():
    """Sets the global value_label to the supplied value"""
    change_value(-1)
    
def add_one():
    """adds one to value"""
    change_value(1)
    
def add_five():
    """Adds five to value"""
    change_value(5)
    

def main():
    """Set up the GUI and run it"""

    global value, value_label
    window = Tk()
    value = 0
    value_label = Label(window, text=str(value))
    value_label.grid(row=0, column=0, columnspan=4)
    subtract_five_button = Button(window, text="-5", command=subtract_five)
    subtract_five_button.grid(row=1, column=0)
    subtract_one_button = Button(window, text="-1", command=subtract_one)
    subtract_one_button.grid(row=1, column=1)
    add_one_button = Button(window, text="+1", command=add_one)
    add_one_button.grid(row=1, column=2)
    add_five_button = Button(window, text="+5", command=add_five)
    add_five_button.grid(row=1, column=3)
    window.mainloop()

main()