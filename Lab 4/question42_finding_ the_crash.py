a = int(input("a "))
b = int(input("b "))

z = 22965892
x = z - a
y = z - b

x += 722
(x, y) = (y, x)

if x >= y:
    z = x - y
else:
    z = x // y

z = z * y 

print(z)

# a = 22966614
# b = 22965893