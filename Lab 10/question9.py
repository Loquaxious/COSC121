class Car:
    """ Defines Car class
    Data Atttibutes: model of type str
                     year of type int
                     speed of type float
    """
    
    def __init__(self, model, year, speed=0):
        """Initialises class Car"""
        self.model = model
        self.year = year
        self.speed = speed
        
    def accelerate(self):
        """Adds 5 to the speed"""
        self.speed += 5''
    
    
    def brake(self):
        """Subtracts 5 from the speed"""
        if self.speed >= 5:
            self.speed -= 5
    
    
    def honk_horn(self):
        """Makes car honk honk"""
        print("{} goes 'beep beep'".format(self.model))
        
        
    def __str__(self):
        """Returns formated string of the Car object"""
        model = self.model
        year = self.year
        speed = self.speed
        template = "{0} ({1}), moving at {2} km/h."
        return template.format(model, year, speed)
    
my_car = Car("Toyota", 1999, 50)
print(my_car)    