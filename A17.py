# Parking Fee Calculation

hours = float(input("Enter number of parking hours: "))

fee = 0

if hours <= 2:
    fee = 30
elif hours <= 5:
    fee = 30 + (hours - 2) * 20
else:
    fee = 30 + (3 * 20) + (hours - 5) * 10

print("Total Parking Fee = Rs.", fee)
