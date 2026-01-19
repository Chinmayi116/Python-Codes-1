# Mobile Recharge Bill Calculation

extra_gb = float(input("Enter extra GB used in the month: "))

bill = 199

if extra_gb > 30:
    bill = bill + 300
else:
    bill = bill + (extra_gb * 20)

print("Total Mobile Recharge Bill = Rs.", bill)
