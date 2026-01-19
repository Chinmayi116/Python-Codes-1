# 16. Palindrome Number Series
n = int(input("Enter n for Palindrome Number Series: "))
print("Palindrome Numbers:", end=" ")
for i in range(1, n+1):
    if str(i) == str(i)[::-1]:
        print(i, end=" ")
print()