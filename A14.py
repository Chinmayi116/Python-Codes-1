# Discount Calculation Program

amount = float(input("Enter total purchase amount: "))

discount = 0

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

print("Discount Amount = Rs.", discount)
print("Final Amount to Pay = Rs.", amount - discount)
