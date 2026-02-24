class BankAccount:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Amount Withdrawn:", amount)

    def display(self):
        print("\n--- Account Details ---")
        print("Account Holder Name:", self.name)
        print("Account Number:", self.acc_no)
        print("Current Balance:", self.balance)


# Main Program
print("---- Bank Account System ----")

name = input("Enter Account Holder Name: ")
acc_no = input("Enter Account Number: ")
balance = float(input("Enter Initial Balance: "))

account = BankAccount(name, acc_no, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Account Details")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)

    elif choice == 3:
        account.display()

    elif choice == 4:
        print("Thank you! Visit Again 😊")
        break

    else:
        print("Invalid Choice! Try Again.")
