n = int(input("Enter the value of n: "))

print("Perfect numbers up to", n, "are:")

for num in range(1, n + 1):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    if sum_div == num and num != 0:
        print(num)
