# ----------------------------------------------------
# Description:
# This program demonstrates abstraction, polymorphism,
# and validation using different payment gateways.
# ----------------------------------------------------

from abc import ABC, abstractmethod


class PaymentGateway(ABC):

    def __init__(self, amount):
        self.amount = amount

    def validate_amount(self):
        return self.amount > 0

    @abstractmethod
    def process_payment(self):
        pass


class UPIPayment(PaymentGateway):

    def process_payment(self):
        print(f"₹{self.amount:.2f} paid successfully through UPI.")


class CardPayment(PaymentGateway):

    def process_payment(self):
        print(f"₹{self.amount:.2f} paid successfully through Card.")


class NetBankingPayment(PaymentGateway):

    def process_payment(self):
        print(f"₹{self.amount:.2f} paid successfully through Net Banking.")


amount = float(input("Enter payment amount: "))

if amount <= 0:
    print("Payment amount must be greater than zero.")

else:

    print("\n1. UPI")
    print("2. Card")
    print("3. Net Banking")

    choice = int(input("Choose payment method: "))

    if choice == 1:
        payment = UPIPayment(amount)

    elif choice == 2:
        payment = CardPayment(amount)

    elif choice == 3:
        payment = NetBankingPayment(amount)

    else:
        payment = None
        print("Invalid payment method.")

    if payment:

        if payment.validate_amount():
            payment.process_payment()
        else:
            print("Invalid payment amount.")