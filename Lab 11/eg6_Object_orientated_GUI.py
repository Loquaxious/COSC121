"""Demonstrate event binding and variable tracing, this time with a clean
   OO design.
"""

from tkinter import *
from tkinter.ttk import *

class GreetingGui:
    """The GUI class"""

    def __init__(self, window):
        """Setup the label and button on given window"""

        self.hello_label = Label(window)
        self.hello_label.grid(row=0, column=0)
        self.hello_button = Button(window,
                                   text="Say hello",
                                   command=self.say_hello)
        self.hello_button.grid(row=1, column=0)


    def say_hello(self):
        """The event handler for clicks on the button"""

        self.hello_label['text'] = "Hello World!"


def main():
    """Set up the GUI and run it."""
    window = Tk()
    greeting_gui = GreetingGui(window)
    window.mainloop()

main()