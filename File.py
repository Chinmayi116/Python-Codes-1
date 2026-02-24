# Writing data to file
file = open("student.txt", "w")

name = input("Enter student name: ")
age = input("Enter age: ")
course = input("Enter course: ")

file.write("Student Name: " + name + "\n")
file.write("Age: " + age + "\n")
file.write("Course: " + course + "\n")

file.close()

print("\nData written successfully!")

# Reading data from file
file = open("student.txt", "r")
print("\n--- Student Details ---")
print(file.read())
file.close()
