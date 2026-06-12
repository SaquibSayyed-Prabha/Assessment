# Q19: Create a BankAccount class and implement encapsulation using private balance variable.
print("Q19: Create a BankAccount class and implement encapsulation using private balance variable.")
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(1000)
print(acc.get_balance())