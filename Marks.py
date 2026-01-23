def student_grade(m1, m2, m3):
    per = (m1 + m2 + m3) / 3

    if per >= 75:
        grade = "Distinction"
    elif per >= 60:
        grade = "First Class"
    elif per >= 50:
        grade = "Second Class"
    elif per >= 35:
        grade = "Pass"
    else:
        grade = "Fail"

    return per, grade

p, g = student_grade(78, 69, 55)
print("Percentage:", p)
print("Grade:", g)
