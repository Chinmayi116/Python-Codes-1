# 15. Digit Sum Series
n = int(input("Enter n for Digit Sum Series: "))
print("Digit Sum Series:", end=" ")
for i in range(1, n+1):
    sum_digits = sum(int(d) for d in str(i))
    print(sum_digits, end=" ")
print()