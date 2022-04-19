class Thing1:
    def __init__(self, x, y):
        self.a = x
        self.b = y

    def __str__(self):
        if self.a == 0 and self.b == 0:
            return 'Empty'
        else:
            return "({}, {})".format(self.a, self.b)

    def __add__(self, other):
        return Thing1(self.a+other.a, self.b+other.b)
    
print(Thing1(2, 4))
print(Thing1(2, 4) + Thing1(3, -1))
print(Thing1(5, -5) + Thing1(-5, 5))

add_em = Thing1(5, -5) + Thing1(-5, 6)
print(type(add_em))