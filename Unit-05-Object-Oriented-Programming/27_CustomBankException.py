# ----------------------------------------------------
# Description:
# This program demonstrates custom exceptions by
# creating an exception for insufficient bank balance.
# ----------------------------------------------------

class InsufficientBalanceError(Exception):
    pass


class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise InsufficientBalanceError(
                "Withdrawal amount exceeds available balance."
            )

        self.__balance -= amount
        print("Withdrawal successful.")
        print(f"Remaining Balance: ₹{self.__balance:.2f}")


balance = float(input("Enter initial balance: ₹"))
amount = float(input("Enter withdrawal amount: ₹"))

account = BankAccount(balance)

try:
    account.withdraw(amount)
except InsufficientBalanceError as error:
    print("Transaction Failed:", error)