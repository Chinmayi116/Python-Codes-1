def is_perfect(num):
    sum_of_factors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i

    return sum_of_factors == num


# Taking input from user
n = int(input("Enter a number: "))

# Check and print result
if is_perfect(n):
    print(n, "is a Perfect Number")
else:
    print(n, "is NOT a Perfect Number")