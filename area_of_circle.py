class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def area(self):
        return Circle.pi * self.r * self.r

    def circum(self):
        return 2 * Circle.pi * self.r

c = Circle(5)
print("Area:", c.area())
print("Circumference:", c.circum())
