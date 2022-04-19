from tkinter import *
from tkinter.ttk import *

class CounterGui:
    """The GUI class"""

    def __init__(self, window):
        """Setup the label and button on given window"""
        
        self.count = 0
        self.label = Label(window, text=self.count)
        self.label.grid(row=0, column=0)
        self.up_button = Button(window, text="+1", command=self.up_count)
        self.up_button.grid(row=1, column=0)
        self.down_button = Button(window, text="-1", command=self.down_count)
        self.down_button.grid(row=1, column=1)
        
    def up_count(self):
        """Adds 1 to the count"""
        self.count += 1
        self.label['text'] = self.count
    
    def down_count(self):
        """Subtracts 1 from the count"""
        self.count -= 1
        self.label['text'] = self.count    
        

def main():
    """Set up the GUI and run it"""
    window = Tk()
    counter_gui = CounterGui(window)
    window.mainloop()

main()