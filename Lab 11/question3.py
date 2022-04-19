from tkinter import *
from tkinter.ttk import *

def label_change1():
    """Changes the text on the buttons"""
    
    message_label['text'] = 'Bonjour!'
    

def label_change2():
    """Changes the text on the buttons"""

    message_label['text'] = 'Au revoir!'
    
    
def main():
    """Construct the GUI and run it"""

    global message_label
    window = Tk()
    message_label = Label(window, text="Click a button!")
    message_label.grid(row=0, column=0)
    
    button1 = Button(window, text='Say hello', command=label_change1) 
    button1.grid(row=1, column=0)
    button2 = Button(window, text='Say goodbye', command=label_change2)
    button2.grid(row=1, column=1)
    window.mainloop()

main()