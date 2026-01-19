# Even Number Series

n = int(input("Enter a value for n: "))

sum_even = 0

print("Even numbers up to", n, "are:")

for i in range(2, n + 1, 2):  # start from 2, step 2
    print(i, end=" ")
    sum_even += i

print("\nSum of even numbers up to", n, "is:", sum_even)
