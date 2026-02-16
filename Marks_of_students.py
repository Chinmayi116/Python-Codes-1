class Student:

    # Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Function to calculate grade
    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

    # Function to display details
    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


# Main Program
name = input("Enter student name: ")
marks = int(input("Enter student marks: "))

# Creating object
s1 = Student(name, marks)

# Calling function
s1.display()
