# Function to check prime number
def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Taking input from user
number = int(input("Enter a number: "))

# Calling the function
if check_prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is Not a Prime Number")
