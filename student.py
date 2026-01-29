# Program to overload + operator for Student class

class Student:
    def __init__(self, name, marks):
        # Initialize student name and marks
        self.name = name
        self.marks = marks

    def __add__(self, other):
        # Add marks and combine names
        new_name = self.name + " + " + other.name
        return Student(new_name, self.marks + other.marks)

    def display(self):
        # Display student details
        print("Name:", self.name, "Total Marks is:", self.marks)

# Create two Student objects
s1 = Student("Asha", 85)
s2 = Student("Ravi", 90)

# Add two students' marks
s3 = s1 + s2

# Display total
s3.display()
