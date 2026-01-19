products = [101, 102, 103, 104, 105]
search_id = int(input("Enter product ID: "))
for p in products:
    if p == search_id:
        print("Product Found")
        break       # Stop searching

