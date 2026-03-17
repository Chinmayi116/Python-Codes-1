import numpy as np
import matplotlib.pyplot as plt

# Student names
students = np.array(["Asha","Ravi","Neha","Arjun","Kiran"])

# Marks
marks = np.array([78, 85, 90, 66, 88])

# Create bar graph
plt.bar(students, marks)

# Graph title and labels
plt.title("Student Marks Graph")
plt.xlabel("Students")
plt.ylabel("Marks")

# Show graph
plt.show()
