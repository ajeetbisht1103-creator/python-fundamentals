# ----------------------------------------------------
# Description:
# This program uses filter() with a helper function
# to extract prime numbers from a list.
# ----------------------------------------------------

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


numbers = list(map(int, input("Enter numbers: ").split()))

prime_numbers = list(filter(is_prime, numbers))

print("Prime Numbers:", prime_numbers)