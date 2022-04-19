def concatenate(strings):
     """Function that concatenates strings"""
     total = "" # Initialise the running total
     for string in strings:
          total = total + string # Add in each new number
     return total

print(concatenate(["x", "yy", "zzz"]))