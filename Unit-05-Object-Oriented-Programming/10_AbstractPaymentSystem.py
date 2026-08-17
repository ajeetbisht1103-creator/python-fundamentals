# ----------------------------------------------------
# Description:
# This program demonstrates abstraction using an
# abstract Payment class and different payment methods.
# ----------------------------------------------------

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount:.2f} using UPI.")


class Card(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount:.2f} using Card.")


class Cash(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount:.2f} using Cash.")


amount = float(input("Enter payment amount: "))

print("\n1. UPI")
print("2. Card")
print("3. Cash")

choice = int(input("Choose payment method: "))

if choice == 1:
    payment = UPI()
elif choice == 2:
    payment = Card()
elif choice == 3:
    payment = Cash()
else:
    payment = None
    print("Invalid choice.")

if payment:
    payment.pay(amount)