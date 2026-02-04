class Student:
    def __init__(self, age):
        self.__age = age   # Private variable

    def show_age(self):
        print("Student Age (Private):", self.__age)

# Create object
s1 = Student(22)

# Access private variable using method
s1.show_age()
