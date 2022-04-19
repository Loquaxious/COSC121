def combine_items(numbers1, numbers2):
    """L"""
    
    results = []
    for i in range(0, len(numbers1)):
        try:
            numbers1[i] * numbers2[i]
        except TypeError:
            results.append(None)
        else:
            results.append(numbers1[i] * numbers2[i])
    
    return results

data1 = [10, 'ug', 30, 40]
data2 = [1, 2, 3, 4]
result = combine_items(data1, data2)
print(result)

list1 = [1, 2.5, 3, 4]
list2 = ['a', 'Uhoh', 2, 3]
result = combine_items(list1, list2)
print(result)