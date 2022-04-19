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
    
    def collect_jujubes(self, number=1):
        """L"""
        
        self.jujubes += number
        return self.jujubes
    
    def eat(self):
        """L"""
        
        if self.jujubes >= 1:
            self.jujubes -= 1
            self.height += 0.2
        else:
            print("I don't have any jujubes to eat!")
    
    def feast(self):
        """L"""
        
        if self.jujubes >= 5:
            self.jujubes -= 5
            if not self.has_nose:
                self.has_nose = True
            else:
                self.height *= 1.5
        else:
            print("I don't have enough jujubes to feast!")


hungry_alien = Taganeran("Jack", 1.89)
hungry_alien.collect_jujubes()
hungry_alien.eat()
print(hungry_alien)    

hungry_alien = Taganeran("Jeff", 1.6)
print(hungry_alien)
hungry_alien.collect_jujubes()
hungry_alien.eat()
print(hungry_alien)

mighty_alien = Taganeran("Tania", 3.14, True)
print("Jujubes: {}".format(mighty_alien.jujubes))
mighty_alien.collect_jujubes(9)
print("Jujubes: {}".format(mighty_alien.jujubes))
mighty_alien.feast()
print("Jujubes: {}".format(mighty_alien.jujubes))
print(mighty_alien)

nice_alien = Taganeran("Lily", 1.11111111111111)
nice_alien.eat()