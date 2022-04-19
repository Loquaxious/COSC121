def display_last(data, n=0):
    """L"""
    
    for num in data[-n:]:
        print(num)
    
data = [1,2,3,4,5,6,7,8,9]
display_last(data, 2)

data = [1,2,3,4,5,6,7,8,9]
display_last(data)