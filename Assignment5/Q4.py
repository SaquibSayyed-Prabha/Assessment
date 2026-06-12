# Q4: Create a BankAccount class with deposit() and withdraw() instance methods.
print("Q4: Create a BankAccount class with deposit() and withdraw() instance methods.")
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(amount, "deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)

# Objects
a1 = BankAccount(1001, "Saquib")
a1.deposit(2000)
a1.withdraw(1000)
a1.check_balance()