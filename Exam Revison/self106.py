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

mighty_alien = Taganeran("Tania", 3.14, True)
mighty_alien.say_hello()