import math
n = int(input("Enter number of terms n for Power-Factorial Series: "))
power_fact_sum = 0
print("Power-Factorial Series:", end=" ")
for i in range(1, n+1):
    x = int(input(f"Enter x{i}: "))
    term = (x ** i) / math.factorial(i)
    print(round(term, 5), end=" ")
    power_fact_sum += term
print("\nSum =", round(power_fact_sum, 5))