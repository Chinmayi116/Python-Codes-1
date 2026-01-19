# Salary Bonus Puzzle

salary = float(input("Enter employee salary: "))
experience = int(input("Enter years of experience: "))

bonus = 0

# Base bonus based on salary
if salary < 20000:
    bonus = salary * 0.20
else:
    bonus = salary * 0.10

# Extra bonus for experience
if experience > 10:
    bonus = bonus + (salary * 0.05)

print("Total Bonus = Rs.", bonus)
print("Total Salary with Bonus = Rs.", salary + bonus)
