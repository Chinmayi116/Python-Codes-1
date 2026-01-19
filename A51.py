balance = 500
while balance > 0:
    amount = int(input("Enter withdrawal amount: "))
    balance -= amount
    if balance <= 0:
        print("Balance is zero")
        break
