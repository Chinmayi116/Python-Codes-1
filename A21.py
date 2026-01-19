# Odd Number Series

n = int(input("Enter a value for n: "))

sum_odd = 0

print("Odd numbers up to", n, "are:")

for i in range(1, n + 1, 2):  # start from 1, step 2
    print(i, end=" ")
    sum_odd += i

print("\nSum of odd numbers up to", n, "is:", sum_odd)
