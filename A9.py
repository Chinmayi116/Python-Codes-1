# Ticket Price Calculation

base_price = 150

weekend = input("Is it weekend? (yes/no): ")
student = input("Are you a student? (yes/no): ")

price = base_price

if weekend.lower() == "yes":
    price = price + 50

if student.lower() == "yes":
    price = price - (price * 0.10)

print("Final Ticket Cost = Rs.", price)
