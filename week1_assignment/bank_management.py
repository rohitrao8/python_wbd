class BankAccount:
    def __init__(self, acc_no, holder_name, balance=0):
        self.__account_number = acc_no
        self.__account_holder = holder_name
        self.__balance = balance


    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    def set_account_number(self, acc_no):
        self.__account_number = acc_no

    def set_account_holder(self, holder_name):
        self.__account_holder = holder_name

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount} into {self.__account_holder}'s account.")
        else:
            print("Deposit amount must be positive.")


    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew ₹{amount} from {self.__account_holder}'s account.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")


    def display_info(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: ₹{self.__balance}")
        print("-" * 40)

accounts = [
    BankAccount("ACC101", "kittu", 5000),
    BankAccount("ACC102", "bamni", 10000),
    BankAccount("ACC103", "siya", 7500),
    BankAccount("ACC104", "laddo", 2000),
    BankAccount("ACC105", "palak", 3000)
]

accounts[0].deposit(1500)
accounts[1].withdraw(3000)
accounts[2].withdraw(8000)  # Insufficient
accounts[3].deposit(-500)   # Invalid
accounts[4].withdraw(1000)


for acc in accounts:
    acc.display_info()

