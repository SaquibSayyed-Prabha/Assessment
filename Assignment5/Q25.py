# Q25: Create a Mini ATM System using encapsulation, constructors, and instance methods.
print("Q25: Create a Mini ATM System using encapsulation, constructors, and instance methods.")
class Account:

    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.__balance = 0

    def verify_password(self, password):
        return self.__password == password

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        self.__balance += amount
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self.__balance -= amount
        print(f"${amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ${self.__balance}")


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        username = input("Enter Username: ")

        if username in self.accounts:
            print("Username already exists.")
            return

        password = input("Create Password: ")
        self.accounts[username] = Account(username, password)

        print("Account created successfully!")
        print("Starting Balance: $0")

    def login(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        if username not in self.accounts:
            print("Account not found.")
            return None

        account = self.accounts[username]

        if account.verify_password(password):
            print(f"Welcome, {username}!")
            return account

        print("Incorrect Password.")
        return None

atm = ATM()
while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")
    if choice == "1":
        atm.create_account()

    elif choice == "2":
        account = atm.login()

        if account:
            while True:
                print("\n===== ACCOUNT MENU =====")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Logout")
                option = input("Enter Choice: ")

                if option == "1":
                    amount = float(input("Enter Amount: "))
                    account.deposit(amount)

                elif option == "2":
                    amount = float(input("Enter Amount: "))
                    account.withdraw(amount)

                elif option == "3":
                    account.check_balance()

                elif option == "4":
                    print("Logged Out Successfully.")
                    break

                else:
                    print("Invalid Choice.")

    elif choice == "3":
        print("Thank You, GoodByee!")
        break

    else:
        print("Invalid Choice.")