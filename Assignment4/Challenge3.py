# Challenge 3: Bank Account System

# Create a BankAccount class.
# Requirements:
# - Create instance variables: account_number, holder_name, balance.
# - Create a class variable bank_name = "State Bank of India".
# - Create instance methods deposit(amount), withdraw(amount), check_balance().
# - Create a class method change_bank_name() to update the bank name.
# - Create multiple account objects and test all methods.

print("Challenge 3: Bank Account System")
print()

class BankAccount:
    bank_name = "SBI"

    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

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

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

# Objects
a1 = BankAccount(1001, "Saquib", 10000)
a2 = BankAccount(1002, "Atharva", 10000)

a1.deposit(2000)
a1.withdraw(1000)
a1.check_balance()

BankAccount.change_bank_name("HDFC")
print("New Bank Name:", BankAccount.bank_name)