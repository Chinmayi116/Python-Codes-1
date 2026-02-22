# Office Stationery Billing Program

# Dictionary to store items and prices
menu = {
    "pen": 10,
    "pencil": 5,
    "eraser": 3,
    "notebook": 50,
    "paper pack": 100,
    "marker": 25,
    "stapler": 80
}

total_bill = 0

print("===== Welcome to Office Stationery Shop =====")
print("\nAvailable Items:")

# Display menu
for item, price in menu.items():
    print(f"{item.title()} - Rs.{price}")

while True:
    product = input("\nEnter the product you want to buy: ").lower()
    
    if product in menu:
        quantity = int(input("Enter quantity: "))
        cost = menu[product] * quantity
        total_bill += cost
        print(f"{product.title()} added to cart. Cost = Rs.{cost}")
    else:
        print("Sorry! Product not available.")
        print("Please reorder from the available menu items.")
        continue
    
    more = input("Do you want to order more items? (yes/no): ").lower()
    if more != "yes":
        break

print("\n===== BILL SUMMARY =====")
print("Total Amount to Pay: Rs.", total_bill)
print("Thank you for shopping with us! 😊")
