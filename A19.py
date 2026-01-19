# Natural Number Series

n = int(input("Enter a value for n: "))

sum_numbers = 0

print("First", n, "natural numbers are:")

for i in range(1, n + 1):
    print(i, end=" ")
    sum_numbers += i

print("\nSum of first", n, "natural numbers is:", sum_numbers)
