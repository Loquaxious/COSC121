class Taganeran:
    """Defines the Taganeran class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_nose of type bool    
    """

    def __init__(self, name, height, has_nose=False):
        """Taganeran constructor"""
        self.name = name
        self.height = height
        self.has_nose = has_nose
        
    def say_hello(self):
        """L"""
        
        if self.has_nose:
            print('HELLO. MY NAME IS {}.'.format(self.name.upper()))
        else:
            print("Hello. My name is {}.".format(self.name))
            
    def __str__(self):
        """L"""
        
        if self.has_nose:
            template = "{0} is a {1:.2f} m tall Taganeran with a nose!"
        else:
            template = "{0} is a {1:.2f} m tall Taganeran!"
        
        return template.format(self.name, self.height)
    
mighty_alien = Taganeran("Tania", 3.14, True)
print(mighty_alien)

first_alien = Taganeran("Jeff", 1.6)
print(first_alien)