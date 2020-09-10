"""
# ProjectEuler.net - Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def prime_factorization(number: int):
    factors = []
    while number % 2 == 0:
        factors.append(2)
        number //= 2

    f = 3
    while f * f <= number:
        if number % f == 0:
            factors.append(f)
            number //= f
        else:
            f += 2
    if number > 1: factors.append(number)
    return factors


if __name__ == "__main__":
    n = 232792560
    prime_factors = prime_factorization(n)
    print(f"The prime factorization of {n} is {prime_factors}.")
    print(f"The largest prime factor of {n} is {max(prime_factors)}.")