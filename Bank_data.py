class Bank:

    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Amount Withdrawn Successfully")

    def show_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)


# Main Program
name = input("Enter Account Holder Name: ")
acc = Bank(name)

while True:
    print("\n1.Deposit\n2.Withdraw\n3.Show Balance\n4.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        amt = int(input("Enter amount to deposit: "))
        acc.deposit(amt)

    elif choice == 2:
        amt = int(input("Enter amount to withdraw: "))
        acc.withdraw(amt)

    elif choice == 3:
        acc.show_balance()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid Choice")
