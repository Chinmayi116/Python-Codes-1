# Function to calculate total and average
def calculate_marks(m1, m2, m3, m4, m5):
    total = m1 + m2 + m3 + m4 + m5
    average = total / 5
    return total, average

# Function to find grade
def find_grade(avg):
    if avg >= 90:
        return "A Grade"
    elif avg >= 75:
        return "B Grade"
    elif avg >= 60:
        return "C Grade"
    elif avg >= 50:
        return "D Grade"
    else:
        return "Fail"

# Main Program
print("---- Student Grade Calculator ----")

name = input("Enter Student Name: ")

m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
m4 = int(input("Enter marks for Subject 4: "))
m5 = int(input("Enter marks for Subject 5: "))

total, average = calculate_marks(m1, m2, m3, m4, m5)
grade = find_grade(average)

print("\nStudent Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
