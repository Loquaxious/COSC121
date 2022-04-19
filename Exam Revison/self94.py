def common(course1, course2, course3):
    """L"""
    course1 = set(course1)
    course2 = set(course2)
    course3 = set(course3)
    
    all3 = course1 & course2 & course3
    
    return all3

c1 = [1, 2, 3, 4, 5]
c2 = [5, 4, 3, 8, 10]
c3 = [2, 3, 5, 8, 10, 12, 4]
for student_id in sorted(common(c1, c2, c3)):
    print(student_id)
    
engr = [4, 6, 3, 5, 10, 11, 8, 9]
cosc = [6, 3, 4, 5, 10, 12, 9, 15, 16]
bifo = [9, 12, 16, 16, 4, 3, 6, 10]
for item in sorted(common(engr, cosc, bifo)):
    print(item)