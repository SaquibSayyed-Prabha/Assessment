# Q6. Create a BankAccount class and derive SavingsAccount, CurrentAccount and FixedDepositAccount classes.
print("Q6. Create a BankAccount class and derive SavingsAccount, CurrentAccount and FixedDepositAccount classes.")
class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def display(self):
        print("Account No :", self.acc_no)
        print("Holder Name:", self.name)
        print("Balance    :", self.balance)

class SavingsAccount(BankAccount):
    def __init__(self, acc_no, name, balance, interest_rate):
        super().__init__(acc_no, name, balance)
        self.interest_rate = interest_rate

    def display_savings(self):
        self.display()
        print("Interest Rate:", self.interest_rate, "%")

class CurrentAccount(BankAccount):
    def __init__(self, acc_no, name, balance, overdraft_limit):
        super().__init__(acc_no, name, balance)
        self.overdraft_limit = overdraft_limit

    def display_current(self):
        self.display()
        print("Overdraft Limit:", self.overdraft_limit)

class FixedDepositAccount(BankAccount):
    def __init__(self, acc_no, name, balance, tenure):
        super().__init__(acc_no, name, balance)
        self.tenure = tenure

    def display_fd(self):
        self.display()
        print("Tenure:", self.tenure, "years")

sa = SavingsAccount("112233", "Saquib", 50000, 4.5)
sa.display_savings()