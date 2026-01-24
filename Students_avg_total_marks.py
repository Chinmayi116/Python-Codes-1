def calculate_marks(marks):
    total = sum(marks)
    average = total / len(marks)
    percentage = (total / (len(marks) * 100)) * 100
    return total, average, percentage


# ---- Main Program ----
n = int(input("Enter number of subjects: "))

marks = []
for i in range(n):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

total, avg, per = calculate_marks(marks)

print("\n--- Student Result ---")
print("Total Marks     :", total)
print("Average Marks   :", avg)
print("Percentage      :", per, "%")
