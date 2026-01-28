class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def peri(self):
        return 2 * (self.l + self.b)

r = Rectangle(5, 4)
print("Area:", r.area())
print("Perimeter:", r.peri())
