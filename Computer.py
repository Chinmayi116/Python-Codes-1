# Function to store and display computer details
def store_computer():
    brand = input("Enter Computer Brand: ")
    processor = input("Enter Processor: ")
    ram = input("Enter RAM Size (in GB): ")
    price = input("Enter Price: ")

    print("\n--- Computer Details ---")
    print("Brand:", brand)
    print("Processor:", processor)
    print("RAM:", ram, "GB")
    print("Price: ₹", price)

# Calling the function
store_computer()
