def get_and_print_rectangle():
    """ Input a rectangle's width and height then print its area """
   
    width_as_str = input("Rectangle width? ")
    height_as_str = input("Rectangle height? ")
    
    width = float(width_as_str)
    height = float(height_as_str)
    
    area = (width * height)
    
    print("The area of the rectangle is: " + str(area))
    
get_and_print_rectangle()
    