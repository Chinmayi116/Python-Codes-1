#Armstrong number
n = int(input("Enter the value of n: "))

print("Armstrong numbers up to", n, "are:")

for num in range(1, n + 1):
    order = len(str(num))
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if sum == num:
        print(num)
