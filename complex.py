# Program to add two Complex numbers using Operator Overloading

class Complex:
    def __init__(self, r, i):
        # Initialize real and imaginary parts
        self.real = r
        self.imag = i

    def __add__(self, other):
        # Overload + operator to add two complex numbers
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def display(self):
        # Display the complex number
        print(self.real, "+", self.imag, "i")

# Create two Complex objects
c1 = Complex(2, 3)
c2 = Complex(4, 5)

# Add two complex numbers
c3 = c1 + c2

# Display result
c3.display()
