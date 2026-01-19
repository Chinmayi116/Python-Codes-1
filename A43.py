# Read the value of n
n = int(input("Enter the value of n: "))

# Loop from 1 to n
for i in range(1, n + 1):
    # Reverse the number using string slicing
    rev = int(str(i)[::-1])

    # Print the reversed number
    print(rev, end=" ")
