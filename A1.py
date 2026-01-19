# Electricity Bill Calculation

units = int(input("Enter the number of units consumed: "))

bill = 0

if units <= 100:
    bill = 150
elif units <= 200:
    bill = 150 + (units - 100) * 3
elif units <= 400:
    bill = 150 + (100 * 3) + (units - 200) * 5
else:
    bill = 150 + (100 * 3) + (200 * 5) + (units - 400) * 7

print("Total Electricity Bill = Rs.", bill)
