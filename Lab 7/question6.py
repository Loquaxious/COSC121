def print_quiz_mark(mark_gained, max_mark=70):
    """Returns grade when given marks"""
    
    precentage = (mark_gained / max_mark) * 100
    print("Your mark: {:.1f}/{:.1f} ({:.1f}%)".format(mark_gained, max_mark, precentage))
    
print_quiz_mark(45.5)
print_quiz_mark(45.5, 105.0)
print_quiz_mark(15, 20)
