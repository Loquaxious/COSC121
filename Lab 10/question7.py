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
        self.speed += 5
    
    
    def brake(self):
        """Subtracts 5 from the speed"""
        if self.speed >= 5:
            self.speed -= 5
    
    
    def honk_horn(self):
        """Makes car honk honk"""
        print("{} goes 'beep beep'".format(self.model))
        
my_car = Car("Toyota", 1975)
print(my_car.speed)        

my_car = Car("Zastava", 2001, 30)
my_car.accelerate()
my_car.accelerate()
my_car.brake()
print(my_car.speed)

my_car = Car("Rust bucket", 1987)
my_car.honk_horn()