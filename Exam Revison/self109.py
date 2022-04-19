class Feeble:
    """L"""
    
    def __init__(self, grade, name, health):
        """L"""
        
        if grade == 'Swiggle':
            self.grade = grade
        elif grade == 'Throve':
            self.grade = grade
        elif grade == 'Plaguelet':
            self.grade = grade
        else:
            raise ValueError('Invalid Feeble grade')
        
        self.name = name
        
        if health < 0:
            self.health = 0
        else:
            self.health = health
        
    def __str__(self):
        """L"""
        
        template = '{} ({}), health = {:.1f}'
        return template.format(self.name, self.grade, self.health)
        
    def pain(self, damage):
        """L"""
        
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return self.health 
        
try:
    oof = Feeble('Famine', 'Fred', 0)
    print(oof)
except ValueError as e:
    print(e)