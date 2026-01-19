# 11. Factorial Series
from math import factorial
n = int(input("Enter n for Factorial Series: "))
fact_sum = 0
print("Factorial Series:", end=" ")
for i in range(1, n+1):
    f = factorial(i)
    print(f, end=" ")
    fact_sum += f
print("\nSum of Factorials =", fact_sum)