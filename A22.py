# Square Number Series

n = int(input("Enter a value for n: "))

sum_squares = 0

print("Square numbers up to", n, "are:")

for i in range(1, n + 1):
    square = i ** 2
    print(square, end=" ")
    sum_squares += square

print("\nSum of squares up to", n, "is:", sum_squares)
