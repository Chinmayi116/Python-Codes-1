class Bank:
    def __init__(self, bal):
        self.bal = bal

    def deposit(self, amt):
        self.bal += amt
        print("Balance:", self.bal)

    def withdraw(self, amt):
        if amt <= self.bal:
            self.bal -= amt
            print("Balance:", self.bal)
        else:
            print("Insufficient balance")

b = Bank(5000)
b.deposit(2000)
b.withdraw(3000)
