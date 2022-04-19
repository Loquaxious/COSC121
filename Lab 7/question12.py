def print_nth_component(data, n):
    """Returns the nth term of a given list"""
    try:
        print(data[n])
    except:
        print("Invalid position provided.")

print_nth_component([10, 20, 30], 0)
print_nth_component([10, 20, 30], 3)
print_nth_component(['bob', 'carol', 'ted', 'alice'], 3)
print_nth_component(['bob', 'carol', 'ted', 'alice'], -6)
