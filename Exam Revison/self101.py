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
        

first_alien = Taganeran("Jeff", 1.6)
first_alien.say_hello()

mighty_alien = Taganeran("Tania", 3.14, True)
mighty_alien.say_hello()