def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Take input from users
num = int(input("Enter a number: "))

# Check and print result
if num > 1 and is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")