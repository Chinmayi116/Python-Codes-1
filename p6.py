class customer:
    account_no = 10001

    def __init__(self):
        self.name = input("Enter your name: ")
        self.balance = 0
        self.acno = customer.account_no
        customer.account_no += 1
        print("Account is created")
        print("Your Account number is", self.acno)

    def deposit(self):
        amount = int(input("Enter amount you want to deposit: "))
        self.balance += amount
        print("Amount deposited successfully")

    def withdraw(self):
        amount = int(input("Enter amount you want to withdraw: "))
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Current balance is:", self.balance)

accounts = {}   

while True:
    print("\n1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        c = customer()
        accounts[c.acno] = c  

    elif ch in [2, 3, 4]:
        ac = int(input("Enter your account number: "))

        if ac in accounts:
            c = accounts[ac]

            if ch == 2:
                c.deposit()
            elif ch == 3:
                c.withdraw()
            elif ch == 4:
                c.check_balance()

        else:
            print("Invalid account number")

    elif ch == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")
