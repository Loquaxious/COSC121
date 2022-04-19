def row_sums(square):
    """returns the sums of each row ina magic square"""
    sum_list = []
    for i in square:
        sum1 = 0
        for n in i:
            sum1 += n 
        sum_list.append(sum1) 
    return sum_list

square = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]
print(row_sums(square))

square1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(row_sums(square1))