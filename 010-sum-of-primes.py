"""
# ProjectEuler.net - Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import floor, sqrt
from numpy import where

def sieve(n: int):
    candidates = [True] * (n+1)
    for i in range(2, floor(sqrt(n) + 1)):
        if candidates[i]:
            for j in range(i**2, n + 1, i):
                candidates[j] = False
    
    return where(candidates)[0][2::]

if __name__ == "__main__":
    n = int(2e6)
    primes = sieve(n)
    print(sum(primes))