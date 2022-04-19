def copy_last(data):
    """Function the copies the last value in a list and appends it without
    changing the original function"""
    original = data
    copy = data[:]
    dbl_last = copy[-1]
    copy.append(dbl_last)
    return copy

print(copy_last([1, 2, 3]))
print(copy_last(['hi']))
      