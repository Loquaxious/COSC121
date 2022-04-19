def sum_first_four(nums):
    """F"""
    if len(nums) < 4:
        state = 0
    else:
        state = sum(nums[0:4])
    return state

student_solution = sum_first_four([1,2,3])
print(student_solution)
student_solution = sum_first_four([5,5,5,5,5,5,5])
print(student_solution)