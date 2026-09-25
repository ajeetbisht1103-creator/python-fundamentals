# ----------------------------------------------------
# Description:
# Demonstrates custom exception handling in Python by
# defining InsufficientFundsError and NegativeAmountError
# classes to validate user account transactions cleanly.
# ----------------------------------------------------


class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds current balance."""

    pass


class NegativeAmountError(Exception):
    """Raised when input amount is negative or zero."""

    pass


class BankAccount:

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise NegativeAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}. Available balance: {self.balance}"
            )

        self.balance -= amount
        print(
            f"Withdrawal successful! Remaining balance for {self.owner}: {self.balance}"
        )


# Demonstration
account = BankAccount(owner="Ajeet", balance=5000.0)

test_amounts = [1500, -200, 6000, 2000]

for amt in test_amounts:
    print(f"\nAttempting to withdraw: {amt}")
    try:
        account.withdraw(amt)
    except NegativeAmountError as e:
        print(f"[Transaction Declined] {e}")
    except InsufficientFundsError as e:
        print(f"[Transaction Declined] {e}")
    finally:
        print("Transaction processing complete.")