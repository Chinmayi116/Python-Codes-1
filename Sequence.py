# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

# Function to calculate e^x
def calculate_ex(x, n):
    sum = 0
    for i in range(n):
        sum = sum + (x ** i) / factorial(i)
    return sum

# Read input from user
x = float(input("Enter the value of x: "))
n = int(input("Enter number of terms (n): "))
result = calculate_ex(x, n)
print("Value of e^", x, "using", n, "terms is:", result)
