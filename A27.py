# 9. Fibonacci Series
n = int(input("Enter n for Fibonacci Series: "))
a, b = 0, 1
fib_sum = 0
print("Fibonacci Series:", end=" ")
for i in range(n):
    print(a, end=" ")
    fib_sum += a
    a, b = b, a + b
print("\nSum =", fib_sum)
