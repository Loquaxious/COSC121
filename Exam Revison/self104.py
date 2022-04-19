class Flunger:
    """Defines FLunger Class.
    Data Attributes: quality of type str
                     name of type str
                     health of type float 
                     
    Methods: 
    """
    
    def __init__(self, quality, name, health):
        """L"""
        if quality == 'Sooglet':
            self.quality = quality
        elif quality == 'Throve':
            self.quality = quality
        elif quality == 'Plaguelet':
            self.quality = quality
        else:
            raise ValueError('Invalid Flunger quality') 
        
        self.name = name
        self.health = health 
        if self.health < 0:
            self.health = 0
        
    def __str__(self):
        """L"""
        
        template = '{} ({}), health = {:.1f}'
        
        return template.format(self.name, self.quality, self.health)
    
    def ouch(self, damage):
        """L"""
        
        self.health -= damage
        
        if self.health < 0:
            self.health = 0

fester = Flunger('Throve', 'Walter', 10.500)
print(fester)

poxer = Flunger('Plaguelet', 'Angus', 0.1)
print(poxer)
peter = Flunger('Sooglet', 'Pedro', 0)
print(peter)

fester = Flunger('Throve', 'Walter', 10.491)
print(fester)
fester.ouch(10.4)
print(fester)
fester.ouch(2)
print(fester)

try:
    oof = Flunger('Famine', 'Fred', 0)
    print(oof)
except ValueError as e:
    print(e)