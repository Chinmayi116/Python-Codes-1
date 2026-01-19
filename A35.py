# 17. Armstrong Number Series
n = int(input("Enter n for Armstrong Number Series: "))
print("Armstrong Numbers:", end=" ")
for i in range(1, n+1):
    num_digits = len(str(i))
    sum_pow = sum(int(d)**num_digits for d in str(i))
    if sum_pow == i:
        print(i, end=" ")
print()
