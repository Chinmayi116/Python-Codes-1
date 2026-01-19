def fib(a, b, n):
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Taking input first
n = int(input("Enter limit: "))
print("Fibonacci Series:")

# Calling function
fib(0, 1, n)

