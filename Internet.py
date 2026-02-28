# Internet Bill Calculation Program

# Input data usage
data = float(input("Enter data usage in GB: "))

bill = 0

# Case 1: Up to 50 GB
if data <= 50:
    bill = 500

# Case 2: 51 to 100 GB
elif data <= 100:
    bill = 500 + (data - 50) * 10

# Case 3: Above 100 GB
else:
    bill = 500 + (50 * 10) + (data - 100) * 15

# Display total bill
print("Total Internet Bill = Rs.", bill)
