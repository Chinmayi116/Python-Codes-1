class Student:
    def __init__(self, name):
        self.name = name   # Public variable

# Create object
s1 = Student("Chinmayi")

# Accessing public variable outside the class
print("Student Name (Public):", s1.name)
