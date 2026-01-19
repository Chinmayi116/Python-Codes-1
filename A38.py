# Read the value of n
n = int(input("Enter the value of n: "))

# Initialize sum to 0
total = 0

# Loop from 1 to n
for i in range(1, n + 1):
    # If number is even, subtract it
    if i % 2 == 0:
        total -= i
    # If number is odd, add it
    else:
        total += i

# Display the result
print("Result of Alternating Series:", total)
