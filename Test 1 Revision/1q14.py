def row_sums(square):
    """L"""
    result = []
    for row in square:
        n = 0
        for num in row:
            n += num 
        result.append(n)        
    return result
square = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]
print(row_sums(square))

square = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(row_sums(square))