# Income Tax Calculation

income = float(input("Enter annual income: "))

tax = 0

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (250000 * 0.05) + (income - 500000) * 0.10
else:
    tax = (250000 * 0.05) + (500000 * 0.10) + (income - 1000000) * 0.20

print("Total Income Tax Payable = Rs.", tax)
