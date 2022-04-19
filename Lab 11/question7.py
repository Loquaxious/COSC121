from tkinter import *
from tkinter.ttk import *

def double_number():
    """Doubles the given number"""
    
    global double_label
    num = int(num_entry.get())
    num *= 2
    double_label['text'] = num
    
def main():
    """Set up the GUI and runs it"""
    
    global num_entry, double_label
    window = Tk()
    
    num_entry = Entry(window)
    num_entry.grid(row=0, column=0)
    
    button = Button(window, text='Double it!', command=double_number)
    button.grid(row=1, column=0)
    
    double_label = Label(window, text='')
    double_label.grid(row=2, column=0)
    
    window.mainloop()

main()