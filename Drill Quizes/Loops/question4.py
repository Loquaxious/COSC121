def list123(nums):
    """L""" 
    for n in range(0, len(nums)):
        if nums[n] == 3:
            if nums[n-1] == 2:
                if nums[n-2] == 1:
                    return True
    return False
    
    
                    
        

print(list123([1, 1, 2, 3, 1]))
print(list123([1, 1, 2, 4, 1]))
