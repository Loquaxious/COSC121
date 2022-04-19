class Taganeran:
    """Defines the Taganeran class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_nose of type bool    
    """

    def __init__(self, name, height, has_nose=False, jujubes=0):
        """Taganeran constructor"""
        self.name = name
        self.height = height
        self.has_nose = has_nose
        self.jujubes = jujubes
        
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
    
    def collect_jujubes(self, number=1):
        """L"""
        
        self.jujubes += number
        return self.jujubes
    
    def eat(self):
        """L"""
        
        if self.jujubes < 1:
            print("I don't have any jujubes to eat!")
        else:
            self.height += 0.2
            self.jujubes -= 1
    
    def feast(self):
        """L"""
        
        if self.jujubes < 5:
            print("I don't have enough jujubes to feast!")
            
        else:
            self.jujubes -= 5
            if self.has_nose:
                self.height *= 1.5
            else:
                self.has_nose = True
    
nice_alien = Taganeran("Lily", 1.11111111111111)
nice_alien.eat()