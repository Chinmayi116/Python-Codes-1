# Geometric Progression (GP) Series

a = float(input("Enter the first term (a): "))
r = float(input("Enter the common ratio (r): "))
n = int(input("Enter the number of terms (n): "))

gp_sum = 0
print("Geometric Progression Series:")

for i in range(n):
    term = a * (r ** i)
    print(term, end=" ")
    gp_sum += term

print("\nSum of the GP =", gp_sum)
