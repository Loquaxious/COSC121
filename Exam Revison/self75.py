def shallow(values):
    for value in values:
        try:
            deep(value)
            print("Through shallow OK")
        except Exception as e:
            print("Oops.", e)
        print("Wow!")

def deep(value):
    try:
        if value == 5:
            raise ValueError("Not today thanks")
        elif value == 0:
            v = 1 / value
        else:
            print("Phew")
    except ZeroDivisionError:
        print("Zero Handled")
    print("Deep exiting")
    
shallow([5, 1, 0])