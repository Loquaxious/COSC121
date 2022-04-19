class Thing1:
    def __init__(self, x, y):
        self.a = 2 * x
        self.b = x + y

    def __str__(self):
        template = (self.b + self.a + self.b + self.a + self.a)
        return template

print(Thing1('3', '5'))
print(Thing1('a', 'b'))