# Library Fine Calculation

days = int(input("Enter number of days book is returned late: "))

fine = 0

if days <= 7:
    fine = 0
elif days <= 14:
    fine = (days - 7) * 2
else:
    fine = (7 * 2) + (days - 14) * 5

print("Total Library Fine = Rs.", fine)
