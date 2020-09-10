"""
# ProjectEuler.net - Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import time
from math import sqrt

def solve_subproblem(m: int = 1000, max_value:int = 1000):
    for a in range(3, m // 3):
        for b in range(a+1, (m-a) // 2):
                if 0 == m**2 + 2 * (a*b - a*m - b*m): 
                    return a, b
                
    return None, None
            

if __name__ == "__main__":
    m = 1000
    start_time = time.time()
    a, b = solve_subproblem(m)
    print("--- %s seconds ---" % (time.time() - start_time))
    c = 1000 - a - b
    print(f"a, b, c = {a}, {b}, {c}")
    print(f"a^2 + b^2 - c^2 = {a**2 + b**2 - c**2}")
    print(f"a * b * c = {a*b*c}")
