def is_old_enough(age):
    """True if age greater than or equal to 18, False otherwise"""
    if age >= 18:
        return "True"
    else:
        return "False"

print(is_old_enough(19))
print(is_old_enough(18))
print(is_old_enough(17))
print(is_old_enough(21))
print(type(is_old_enough(19)))
print(type(is_old_enough(17)))  