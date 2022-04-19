class Thing:
    
    def __init__(self, x, y):
        self.a = x
        self.b = y
        
    def __str__(self):
        return "{}, {}".format(self.a, self.b)
    
    def mangle(self):
        temp = self.a
        self.a = self.b + self.a + self.a +self.b
        self.b = temp + self.b + self.b + temp

def gaga(obj):
    obj.mangle()
    print(obj)

obj = Thing('y','x')
gaga(obj)