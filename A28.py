# 10. Prime Number Series
n = int(input("Enter n to display prime numbers up to n: "))
print("Prime Numbers:", end=" ")
prime_sum = 0
for num in range(2, n+1):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        prime_sum += num
print("\nSum of Primes =", prime_sum)