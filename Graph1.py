import matplotlib.pyplot as plt

students = ["A","B","C","D"]
marks = [60,75,80,90]

plt.bar(students, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
