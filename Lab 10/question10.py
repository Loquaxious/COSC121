class Blork:
    """Defines the Blork class
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool
                     baranges of type int
    """
    
    def __init__(self, name, height, has_horns=False, baranges=0):
        """Creates a new Blork object"""
        self.name = name
        self.height = height
        self.has_horns = has_horns
        self.baranges = baranges
    
    
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
        
    
    def collect_baranges(self, number=1):
        """Add a given number of baranges to the Blork's number"""
        self.baranges += number
    
    
    def eat(self):
        """Consumes 1 barange and grows Bork"""
        if self.baranges >= 1:
            self.baranges -= 1
            self.height += 0.1
        else:
            print("I don't have any baranges to eat!")
    
    
    def feast(self):
        """Consumes 5 baranges and grows Bork"""
        if self.baranges >= 5:
            self.baranges -= 5
            if self.has_horns == False:
                self.has_horns = True
            else:
                self.height *= 1.5
        else:
            print("I don't have enough baranges to feast!")
            
        
hungry_blork = Blork("Jack", 1.89)
hungry_blork.collect_baranges()
hungry_blork.eat()
print(hungry_blork)        

hungry_blork = Blork("Jeff", 1.6)
print(hungry_blork)
hungry_blork.collect_baranges()
hungry_blork.eat()
print(hungry_blork)

mighty_blork = Blork("Chewblorka", 3.14, True)
print("Baranges: {}".format(mighty_blork.baranges))
mighty_blork.collect_baranges(9)
print("Baranges: {}".format(mighty_blork.baranges))
mighty_blork.feast()
print("Baranges: {}".format(mighty_blork.baranges))
print(mighty_blork)

nice_blork = Blork("Lily", 1.11111111111111)
nice_blork.eat()