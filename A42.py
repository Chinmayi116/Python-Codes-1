# Read the value of n
n = int(input("Enter the value of n: "))

# Loop from 1 to n
for i in range(1, n + 1):
    # Stop execution if number is a multiple of 7
    if i % 7 == 0:
        break

    # Skip the number if it is a multiple of 3
    if i % 3 == 0:
        continue

    # Print the number
    print(i, end=" ")
