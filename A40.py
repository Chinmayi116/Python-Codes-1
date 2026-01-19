# Read number of terms
n = int(input("Enter number of terms: "))

# Display the series
print("Number Pattern Series:")

# Loop to generate pattern
for i in range(1, n + 1):
    # Formula to generate series term
    print(i * (i + 1), end=" ")
