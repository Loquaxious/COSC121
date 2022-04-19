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
self.name_keys = []
for name_str in self.blorks.keys():
self.name_keys.append(name_str)
# Combo Box
# Your combo box code goes here   
self.combobox = Combobox(window,
values=self.name_keys,
font=("Arial", 10))
self.combobox.set("")
self.combobox.grid(row=0, column=0)

# View Button
# Your button code goes here
self.view_button = Button(window,
text='View detail',
command= self.view)
self.view_button.grid(row=0, column=1)

# Details Label
# Your label code goes here
self.detail_label = Label(window, text="Press 'view detail'")
self.detail_label.grid(row=1, column=0, padx=20)


# Your button function goes here
def view(self):
"""view the detail"""
blork_object = self.blorks[self.combobox.get()] # dict
if self.combobox.get() == "":
self.datail_label['text'] = TEMPLATE.format("Press 'view detail'")
else:
if blork_object.has_horn == True:
self.datail_label['text'] = TEMPLATE.format(blork_object.name, blork_object.height, "Yes")
  
else:
if blork_object.has_horn == False:
self.datail_label['text'] = TEMPLATE.format(blork_object.name, blork_object.height, "No")
  
  
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