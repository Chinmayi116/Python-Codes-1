# '''Create a Python program to simulate a bank account system with the following functionalities:
# 1.	Create Account: Create a new account with a unique account number, account holder's name, and initial balance.
# 2.	Deposit Money: Deposit money into the account.
# 3.	Withdraw Money: Withdraw money from the account if sufficient balance exists.
# 4.	Check Balance: Check the current balance of the account.
# 5.	Display Account Details: View account details like account number, holder's name, and balance.
# 6.	Menu-Driven: Implement a menu where users can select options to perform these tasks.
# The program should continue running until the user chooses to exit.
# '''
class BankAccount:
    # Class variable to generate unique account numbers
    account_number_counter = 1000

    def __init__(self, account_holder, initial_balance=0):
        # Private data members (Encapsulation)
        self.__account_holder = account_holder
        self.__balance = initial_balance
        self.__account_number = BankAccount.account_number_counter
        BankAccount.account_number_counter += 1

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited Amount:", amount)
        else:
            print("Invalid deposit amount")

    # Withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn Amount:", amount)
        else:
            print("Invalid withdrawal or insufficient balance")

    # Check balance
    def check_balance(self):
        return self.__balance

    # Display account details
    def display_account(self):
        print("Account Number:", self.__account_number)
        print("Account Holder Name:", self.__account_holder)
        print("Account Balance:", self.__balance)

    # Get account number
    def get_account_number(self):
        return self.__account_number


# Dictionary to store accounts
accounts = {}

# Menu-driven program
while True:
    print("\n----- Bank Account Menu -----")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter account holder name: ")
        balance = float(input("Enter initial balance: "))
        account = BankAccount(name, balance)
        accounts[account.get_account_number()] = account
        print("Account created successfully!")
        print("Your Account Number is:", account.get_account_number())

    elif choice == 2:
        acc_no = int(input("Enter account number: "))
        if acc_no in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[acc_no].deposit(amount)
        else:
            print("Account not found")

    elif choice == 3:
        acc_no = int(input("Enter account number: "))
        if acc_no in accounts:
            amount = float(input("Enter amount to withdraw: "))
            accounts[acc_no].withdraw(amount)
        else:
            print("Account not found")

    elif choice == 4:
        acc_no = int(input("Enter account number: "))
        if acc_no in accounts:
            print("Current Balance:", accounts[acc_no].check_balance())
        else:
            print("Account not found")

    elif choice == 5:
        acc_no = int(input("Enter account number: "))
        if acc_no in accounts:
            accounts[acc_no].display_account()
        else:
            print("Account not found")

    elif choice == 6:
        print("Thank you! Exiting the program.")
        break

    else:
        print("Invalid choice, please try again")

