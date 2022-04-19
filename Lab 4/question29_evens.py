def evens(numbers):
    """Returns all the even numbers in the given list"""
    even = []
    
    for num in numbers:
        if ((num % 2) == 0):
            even.append(num)
    return even 

print(evens([1, 2, 3, 4, 5, 6, 10, 11]))