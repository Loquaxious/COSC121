def print_nth_component(data, n):
    """L"""
    try:
        data[n]
    except IndexError:
        print('Invalid position provided.')
    else:
        print(data[n])

print_nth_component([10, 20, 30], 0)
print_nth_component([10, 20, 30], 3)
print_nth_component(['bob', 'carol', 'ted', 'alice'], 3)
print_nth_component(['bob', 'carol', 'ted', 'alice'], -6)
