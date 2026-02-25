# Function to subtract two numbers
def subtract_numbers(a, b):
    result = a - b
    return result

# Main Program
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

answer = subtract_numbers(num1, num2)

print("Subtraction of two numbers is:", answer)
