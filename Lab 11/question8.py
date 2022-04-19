from tkinter import *
from tkinter.ttk import * 

def process_numbers():
    """Does some stuff to the numbers based off inputs"""
    global label
    
    num1 = int(num_entry1.get())
    num2 = int(num_entry2.get())
    
    if sign_combobox.get() == '+':
        label['text'] = "={}".format((num1 + num2))
    elif sign_combobox.get() == '-':
        label['text'] = "={}".format((num1 - num2))
    elif sign_combobox.get() == '*':
        label['text'] = "={}".format((num1 * num2))
    

def main():
    """Sets up and runs the GUI"""
    
    global num_entry1, sign_combobox, num_entry2, label 
    window = Tk()
    
    num_entry1 = Entry(window)
    num_entry1.grid(row=0, column=0)
    
    sign_options = ["+", "-", "*"]
    sign_combobox = Combobox(window,\
                             values = sign_options,\
                             font=("Arial", 10))
    sign_combobox.set("+")
    sign_combobox.grid(row=0, column=1)
    
    num_entry2 = Entry(window)
    num_entry2.grid(row=0, column=2)
    
    label = Label(window, text ='')
    label.grid(row=0, column=3)
    
    button = Button(window, text="Calculate", command=process_numbers)
    button.grid(row=1, column=1)
    
    window.mainloop()

main()