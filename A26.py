# Harmonic Series

n = int(input("Enter the number of terms (n): "))

harmonic_sum = 0
print("Harmonic Series:")

for i in range(1, n + 1):
    term = 1 / i
    print(f"1/{i}", end=" " if i < n else "")
    harmonic_sum += term

print("\nSum of Harmonic Series =", harmonic_sum)

