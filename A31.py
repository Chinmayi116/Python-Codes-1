import math
# 13. Reciprocal Factorial Series
n = int(input("Enter n for Reciprocal Factorial Series: "))
recip_fact_sum = 0
print("Reciprocal Factorial Series:", end=" ")
for i in range(1, n+1):
    term = 1 / math.factorial(i)
    print(round(term, 5), end=" ")
    recip_fact_sum += term
print("\nSum =", round(recip_fact_sum, 5))

