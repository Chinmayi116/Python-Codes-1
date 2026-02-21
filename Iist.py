# List Operations Program

numbers = []

while True:
    print("\n----- LIST OPERATIONS -----")
    print("1. Add Element")
    print("2. Insert Element")
    print("3. Remove Element")
    print("4. Display List")
    print("5. Find Maximum and Minimum")
    print("6. Sort List")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        n = int(input("Enter number to add: "))
        numbers.append(n)
        print("Element added successfully!")

    elif choice == '2':
        n = int(input("Enter number to insert: "))
        pos = int(input("Enter position: "))
        numbers.insert(pos, n)
        print("Element inserted successfully!")

    elif choice == '3':
        n = int(input("Enter number to remove: "))
        if n in numbers:
            numbers.remove(n)
            print("Element removed successfully!")
        else:
            print("Element not found!")

    elif choice == '4':
        print("Current List:", numbers)

    elif choice == '5':
        if len(numbers) > 0:
            print("Maximum:", max(numbers))
            print("Minimum:", min(numbers))
        else:
            print("List is empty!")

    elif choice == '6':
        numbers.sort()
        print("List sorted successfully!")

    elif choice == '7':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
