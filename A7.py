# Courier Charges Calculation

weight = float(input("Enter parcel weight in kg: "))

cost = 0

if weight <= 1:
    cost = 50
elif weight <= 5:
    cost = 50 + (weight - 1) * 30
else:
    cost = 50 + (4 * 30) + (weight - 5) * 20

print("Total Courier Cost = Rs.", cost)
