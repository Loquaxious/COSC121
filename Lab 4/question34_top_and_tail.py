def top_and_tail(string):
    """Returns the given string without first and last characters"""
    sub_string = string[1:-1]
    return sub_string

print(top_and_tail('stubby'))
print(top_and_tail('another test string'))