class Whatsit:
    """Defines the Whatsit class
       Data attributes: grade of type str
                        name of trpe str
                        health of type float
    """
    
    def __init__(self, grade, name, health):
        """Creates new Whatsit object"""
        if grade == 'Grubling':
            self.grade = grade
        elif grade == 'Throve':
            self.grade = grade
        elif grade == 'Plaguelet':
            self.grade = grade
        else:
            raise ValueError('Invalid Whatsit grade')
        
        self.name = name
        
        if health < 0:
            self.health = 0
        else:
            self.health = health
        
    def __str__(self):
        """Returns a formatted string of the object Whatsit"""
        grade = self.grade
        name = self.name
        health = self.health
        template = '{0} ({1}), health = {2:.1f}'
        return template.format(name, grade, health)
    
    def hurt(self, suffering=0):
        """Returns amount of health after amount of suffering"""
        self.health -= suffering
        if self.health < 0:
            self.health = 0
            return self.health
        else:
            return self.health

fester = Whatsit('Throve', 'Walter', 10.500)
print(fester)

poxer = Whatsit('Plaguelet', 'Angus', 0.1)
print(poxer)
peter = Whatsit('Grubling', 'Pedro', 0)
print(peter)

fester = Whatsit('Throve', 'Walter', 10.491)
print(fester)
fester.hurt(10.4)
print(fester)
fester.hurt(2)
print(fester)

try:
    oof = Whatsit('Famine', 'Fred', 0)
    print(oof)
except ValueError as e:
    print(e)