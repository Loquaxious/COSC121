def print_section(size):
    """Returns a wedge of asterisks of a given size"""
    for i in range(size, 0, -1):
        ans = i * "*"
        print(ans)

print("-------------------------")
print_section(1)
print("-------------------------")
print_section(2)
print("-------------------------")
print_section(4)
print("-------------------------")
print_section(3)
print("-------------------------")