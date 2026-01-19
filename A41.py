# Read number of prime Fibonacci terms
n = int(input("Enter number of terms: "))

# Initialize first two Fibonacci numbers
a, b = 0, 1

# Counter for prime Fibonacci numbers
count = 0

# Display heading
print("Prime Fibonacci numbers:")

# Loop until required number of terms are found
while count < n:
    # Generate next Fibonacci number
    a, b = b, a + b

    # Check if Fibonacci number is greater than 1
    if a > 1:
        # Assume number is prime
        is_prime = True

        # Check divisibility
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                is_prime = False
                break

        # If number is prime, print it
        if is_prime:
            print(a, end=" ")
            count += 1
