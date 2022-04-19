from tkinter import *
from tkinter.ttk import *

VOWELS = ['a', 'e', 'i', 'o', 'u']
MESSAGE_TEMPLATE = "{0}\nThar be {1} vowels in me greetin`!"

def change_message(greeting):
    """Set the global message_label to the supplied greeting, followed
       by a count of the number of vowels in the greeting.
    """

    global message_label
    number_vowels = 0
    for letter in greeting.lower():
        if letter in VOWELS:
            number_vowels += 1
    message_label['text'] = MESSAGE_TEMPLATE.format(greeting, number_vowels)

def ahoy():
    """Command handler for the Greeting 1 button"""
    change_message("Ahoy!")

def avast():
    """Command handler for the Greeting 2 button"""
    change_message("Avast ye!")

def aye():
    """Command handler for the Greeting 3 button"""
    change_message("Aye aye!")

def main():
    """Set up the GUI and run it"""

    global message_label
    window = Tk()
    message_label = Label(window, text='')
    message_label.grid(row=1, column=0, columnspan=3)
    ahoy_button = Button(window, text="Greeting 1", command=ahoy)
    ahoy_button.grid(row=0, column=0)
    avast_button = Button(window, text="Greeting 2", command=avast)
    avast_button.grid(row=0, column=1)
    aye_button = Button(window, text="Greeting 3", command=aye)
    aye_button.grid(row=0, column=2)
    window.mainloop()

main()