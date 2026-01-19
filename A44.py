# Read the value of x and n
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

# Initialize total sum
total = 0

# Function to calculate factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

# Loop to calculate each term contribution
for i in range(n + 1):
    term = factorial(x + i)
    total += term

    # Display each term contribution
    print(f"Contribution of term {(x+i)}! = {term}")

# Display final sum
print("Total sum of the series:", total)
