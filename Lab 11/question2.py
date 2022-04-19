from tkinter import *
from tkinter.ttk import *

def main():
    """An Arrangment of fruit labels"""
    window = Tk()
    apple_label = Label(window, text='Apple')
    apple_label.grid(row=2, column=1)
    banana_label = Label(window, text='Banana')
    banana_label.grid(row=1, column=0)
    orange_label = Label(window, test='Orange')
    orange_label.grid(row=2, column=2)
    mango_label = Label(window, text='Mango')
    mango_label.grid(row=0, column=1)
    window.mainloop()

main()