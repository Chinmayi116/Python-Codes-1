# Dictionary Program

student = {}

while True:
    print("\n----- DICTIONARY OPERATIONS -----")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Delete Student")
    print("5. Update Marks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        student[name] = marks
        print("Student added successfully!")

    elif choice == '2':
        name = input("Enter student name to search: ")
        if name in student:
            print(name, "has scored", student[name], "marks")
        else:
            print("Student not found!")

    elif choice == '3':
        if len(student) == 0:
            print("Dictionary is empty!")
        else:
            print("\nStudent Records:")
            for key, value in student.items():
                print("Name:", key, "| Marks:", value)

    elif choice == '4':
        name = input("Enter student name to delete: ")
        if name in student:
            del student[name]
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == '5':
        name = input("Enter student name to update marks: ")
        if name in student:
            marks = float(input("Enter new marks: "))
            student[name] = marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    elif choice == '6':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
