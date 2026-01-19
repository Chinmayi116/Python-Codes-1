# Read the value of n
n = int(input("Enter the value of n: "))

# If input is invalid, terminate the program
if n <= 0:
    print("Invalid input. Program terminated.")
    exit()

# Loop from 1 to n
for i in range(1, n + 1):

    # Skip multiples of 3 (invalid data)
    if i % 3 == 0:
        continue

    # Stop loop when a multiple of 7 is found
    if i % 7 == 0:
        print("Multiple of 7 encountered. Loop stopped.")
        break

    # Print valid numbers
    print(i, end=" ")
