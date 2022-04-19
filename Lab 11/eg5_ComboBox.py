from tkinter import *
from tkinter.ttk import *

def main():
    window = Tk()
    fruit_choices = ["Apple", "Banana", "Cherry", "Dragon Fruit"]
    fruit_combobox = Combobox(window,
                              values=fruit_choices,
                              font=("Arial", 10))
    fruit_combobox.set('Apple')
    fruit_combobox.grid(row=0, column=0, padx=20, pady=40)
    window.mainloop()

main()