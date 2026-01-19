import math  # Make sure to import math module

# 12. Shifted Factorial Series
x = int(input("Enter starting number x for Shifted Factorial Series: "))
n = int(input("Enter number of terms n: "))
shift_fact_sum = 0
print("Shifted Factorial Series:", end=" ")
for i in range(x, x + n):
    f = math.factorial(i)
    print(f, end=" ")
    shift_fact_sum += f
print("\nSum =", shift_fact_sum)
