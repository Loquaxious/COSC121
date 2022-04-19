def column_sums(square):
    """L"""
    
    sum_list = []
    
    for i in range(0, len(square[0])):
        sum1 = 0
        for row in square:
            sum1 += row[i]
        sum_list.append(sum1)
    return sum_list

square = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(column_sums(square))        