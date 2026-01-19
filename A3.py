# Internet Bill Calculation

data = float(input("Enter data usage in GB: "))

bill = 0

if data <= 50:
    bill = 500
elif data <= 100:
    bill = 500 + (data - 50) * 10
else:
    bill = 500 + (50 * 10) + (data - 100) * 15

print("Total Internet Bill = Rs.", bill)
