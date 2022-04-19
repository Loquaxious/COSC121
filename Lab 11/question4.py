from tkinter import *
from tkinter.ttk import *

def up_count():
    """Adds 1 to the count"""
    global current_count
    current_count += 1
    label['text'] = current_count

def down_count():
    """Subtracts 1 from the count"""
    global current_count
    current_count -= 1
    label['text'] = current_count

def main():
    """hey dude"""
    global label, current_count
    current_count = 0
    window = Tk()
    
    label = Label(window, text=current_count)
    label.grid(row=0, column=0)
    
    up_button = Button(window, text='+1', command=up_count)
    up_button.grid(row=1, column=0)
    
    down_button = Button(window, text='-1', command=down_count)
    down_button.grid(row=1, column=1)
    window.mainloop()

main()