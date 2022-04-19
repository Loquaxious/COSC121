"""A program that defines an Automobile class and then tests it"""
class Automobile: # Hint: How do you declare a class?
    """Defines an Automobile class.
    Data attributes: is_driving of type bool
    Methods: go()
    """

    def __init__(self):
        """Creates a new Automobile object"""
        self.is_driving = False
    
    def go(self):
        """Makes the automobile start driving"""
        self.is_driving = True
        print("Vrooom!")
        
def main():
    """Main function tests the Automobile class"""
    my_car = Automobile() # Hint: Create an Automobile instance
    print(type(my_car))      # Print its type
    print(my_car.is_driving) # Print whether it's going
    Automobile.go(my_car)  # Hint: Use your car's go method
    print(my_car.is_driving) 

main()