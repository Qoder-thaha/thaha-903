
class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("amount deposited:", amount)
        print("updated balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient balance!")
        else:
            self.balance -= amount
            print("amount withdrawn:", amount)
            print("updated balance:", self.balance)


acc_no = input("enter account number:")
name = input("enter name:")
acc_type = input("enter account type:")
balance = float(input("enter initial balance:"))

account = BankAccount(acc_no, name, acc_type, balance)

deposit_amount = float(input("enter amount to deposit:"))
account.deposit(deposit_amount)

withdrawn_amount = float(input("enter amount to withdraw:"))
account.withdraw(withdrawn_amount)
