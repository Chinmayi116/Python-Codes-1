class Complex:
    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img

    def add(self, other):
        real_part = self.real + other.real
        img_part = self.img + other.img
        return Complex(real_part, img_part)

    def display(self):
        print(f"{self.real} + {self.img}i")


# Objects
c1 = Complex(2, 3)
c2 = Complex(9, 8)

# Calling normal method
c3 = c1.add(c2)
c3.display()
