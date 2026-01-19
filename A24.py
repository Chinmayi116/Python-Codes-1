# Arithmetic Progression (AP) Series

a = int(input("Enter the first term (a): "))
d = int(input("Enter the common difference (d): "))
n = int(input("Enter the number of terms (n): "))

print("AP Series:")

for i in range(n):
    term = a + i * d
    print(term, end=" ")

# Optional: Sum of AP series
sum_ap = (n * (2*a + (n-1)*d)) / 2
print("\nSum of AP series:", int(sum_ap))
