# Read number of terms
n = int(input("Enter number of terms: "))

# Initialize sum to 0
total = 0

# Loop through each term
for i in range(1, n + 1):
    # If term is odd, add square
    if i % 2 != 0:
        total += i ** 2
    # If term is even, add cube
    else:
        total += i ** 3

# Display the final sum
print("Sum of Mixed Series:", total)
