"""
# ProjectEuler.net - Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def is_prime(number: int):
    # trivial checks
    if number <= 1:
        return False
    elif number == 2:
        return True

    if number % 2 == 0:
        return False

    # non-trivial checks
    # exploit two facts:
    # - prime factors can only be odd
    # - only one prime factor can be greater than sqrt(number)

    factor = 3
    while factor * factor <= number:
        if number % factor == 0:
            return False
        else:
            factor += 2
    
    return True

def get_prime(number: int):
    counter, i = 0, 0
    while counter < number:
        i += 1
        if is_prime(i):
            counter +=1
            # print(i)
        
    return i


if __name__ == "__main__":
    n = 10001
    prime_factors = is_prime(n)
    print(f"The number {n} is prime? {prime_factors}.")
    print(f"Prime number #{n} is {get_prime(n)}.")