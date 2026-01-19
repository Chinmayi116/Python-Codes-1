def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


# Taking input from user
num = int(input("Enter a number: "))

# Calling the function and printing result
print("Factorial of", num, "is", factorial(num))