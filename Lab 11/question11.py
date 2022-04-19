from tkinter import *
from tkinter.ttk import *

TEMPLATE = "Name: {0}\nHeight: {1:.2f} m\nHorns: {2}"

class Blork(object):
    """Defines the Blork class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool    
    """

    def __init__(self, name, height, has_horns=False):
        """Blork constructor"""
        self.name = name
        self.height = height
        self.has_horns = has_horns
        

class BlorkGui(object):
    """Defines the Blork Interface"""
    
    def __init__(self, window, blorks):
        """Setup the label and button on given window"""
        self.blorks = blorks
        
        # Combo Box
        names = []
        for key in self.blorks:
            names.append(key)
            
        self.combobox = Combobox(window, values=names, font=('Arial', 10))
        self.combobox.set(names[0])
        self.combobox.grid(row=0, column=0)
        
        # View Button
        self.button = Button(window, text='View details', command=self.disp_details)
        self.button.grid(row=0, column=1)
        
        # Details Label
        self.label = Label(window, text="Press 'View details'") 
        self.label.grid(row=1, column=0)
        
    def disp_details(self):
        """Displays the details of a Blork provided"""
        name = self.combobox.get()
        blork =self.blorks[name]
        name = blork.name
        height = blork.height
        has_horns = blork.has_horns
        
        if has_horns == False:
            horns = 'No'
        else:
            horns = 'Yes'
        self.label['text'] = TEMPLATE.format(name, height, horns)

def main():
    """Set up the GUI and run it."""    
    blork_dict = {"Jeff": Blork("Jeff", 1.6),
              "Lily": Blork("Lily", 1.111111),
              "Jack": Blork("Jack", 1.89),
              "Chewblorka": Blork("Chewblorka", 3.14, True),
              "Blorkstien": Blork("Blorkstien", 0.856, True)}
    window = Tk()
    blork_gui = BlorkGui(window, blork_dict)
    window.mainloop()

main()