# ----------------------------------------------------
# Description:
# This program demonstrates encapsulation through
# a bank account class with deposit and withdrawal
# operations.
# ----------------------------------------------------

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Current Balance: ₹{self.balance:.2f}")


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, balance)

deposit = float(input("Enter deposit amount: "))
account.deposit(deposit)

withdraw = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw)

account.display_balance()