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
        """say hello"""
        if self.has_nose:
            template = 'HELLO. MY NAME IS {}.'
            print(template.format(self.name.upper()))
        else:
            template = 'Hello. My name is {}.'
            print(template.format(self.name))    
    
    def __str__(self):
        """L"""
        
        if self.has_nose:
            template = '{0} is a {1:.2f} m tall Taganeran with a nose!'
        else:
            template = '{0} is a {1:.2f} m tall Taganeran!'
        
        return template.format(self.name, self.height)
    
first_alien = Taganeran("Jeff", 1.6)
print(first_alien)    

mighty_alien = Taganeran("Tania", 3.14, True)
print(mighty_alien)