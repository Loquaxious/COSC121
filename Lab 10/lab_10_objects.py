"""File for creating Person objects"""

class Person:
    """Defines a Person class, suitable for use in a hspital context.
    Data Attributes: name of type str
                     age of type int
                     weight (kg) of type float
                     height (metres) of type float
    Methods: bmi()
    """
    
    def __init__(self, name, age, weight, height):
        """Creates a new Person object with the specified name, age, weight, 
           and height"""
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        
    def bmi(self):
        """Returns the body mass index of the person"""
        return self.weight / (self.height * self.height)
    
    
    def status(self):
        """Returns status based off BMI results"""
        bmi_value = self.bmi()
        if bmi_value < 18.5:
            status1 = "Underweight"
        elif bmi_value >= 18.5 and bmi_value < 25:
            status1 = "Normal"
        elif bmi_value >= 25 and bmi_value < 30:
            status1 = "Overweight"
        else:
            status1 = "Obese"
        
        return status1    
    
    
    def __str__(self):
        """Returns the formatted string represent of the Person object"""
        name = self.name
        age = self.age
        bmi = self.bmi()
        status = self.status()
        template = "{0} ({1}) has a bmi of {2:3.2f}. Their status is {3}."
        return template.format(name, age, bmi, status)