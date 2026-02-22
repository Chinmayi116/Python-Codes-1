# Function to find factorial
def find_factorial():
    try:
        num = int(input("Enter a non-negative integer: "))
        
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
            return
        
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        
        print("Factorial of", num, "is", fact)
    
    except ValueError:
        print("Error: Please enter a valid integer only.")


# Function to reverse a number
def reverse_number():
    try:
        num = int(input("Enter an integer to reverse: "))
        
        reversed_num = 0
        temp = abs(num)
        
        while temp > 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10
        
        # Handle negative numbers
        if num < 0:
            reversed_num = -reversed_num
        
        print("Reversed number is:", reversed_num)
    
    except ValueError:
        print("Error: Please enter a valid integer only.")


# Main menu
while True:
    print("\n--- MENU ---")
    print("1. Find Factorial")
    print("2. Reverse a Number")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        find_factorial()
    elif choice == '2':
        reverse_number()
    elif choice == '3':
        print("Program exited successfully.")
        break
    else:
        print("Error: Invalid choice! Please select between 1 and 3.")
