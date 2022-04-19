class Blork:
    """Defines the Blork class
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool
    """
    
    def __init__(self, name, height, has_horns=False):
        """Creates a new Blork object"""
        self.name = name
        self.height = height
        self.has_horns = has_horns
    
    def say_hello(self):
        """Prints a greeting to the Blork"""
        if self.has_horns == False:
            print("Hi! My name is {}!".format(self.name))
        else:
            print("HI! MY NAME IS {}!".format((self.name).upper()))
            
    def __str__(self):
        """Returns formmated string of the Blork object"""
        horns = self.has_horns
        name = self.name
        height = self.height
        
        if horns == False:
            template = "{0} is a {1:.2f} m tall blork!"
            return template.format(name, height)
        else:
            template = "{0} is a {1:.2f} m tall horned blork!"
            return template.format(name, height)
            
first_blork = Blork("Jeff", 1.6)
print(first_blork)            

mighty_blork = Blork("Chewblorka", 3.14, True)
print(mighty_blork)