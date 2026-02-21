class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)


# List to store student objects
students = []

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    
    s = Student(roll, name, marks)
    students.append(s)
    print("Student added successfully!")

def display_students():
    if len(students) == 0:
        print("No students found!")
    else:
        for s in students:
            s.display()

def search_student():
    roll = int(input("Enter Roll Number to search: "))
    for s in students:
        if s.roll_no == roll:
            s.display()
            return
    print("Student not found!")

# Menu
while True:
    print("\n----- Student Management System -----")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        print("Thank you! Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
