def combine_values(numbers1, numbers2):
    """L"""
    
    data = []
    
    for num in range(0, len(numbers1)):
        try:
            numbers1[num] - numbers2[num]
        except TypeError:
            data.append(None)
        except ValueError:
            data.append(None)
        else:
            data.append(numbers1[num] - numbers2[num])
    return data        
    

data1 = [10, 'ug', 30, 40]
data2 = [1, 2, 3, 4]
result = combine_values(data1, data2)
print(result)

list1 = [1, 2, 3, 4]
list2 = ['a', 'Uhoh', 2, 3]
result = combine_values(list1, list2)
print(result)