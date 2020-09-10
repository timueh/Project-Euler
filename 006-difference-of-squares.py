"""
# ProjectEuler.net - Problem 6

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def my_sum(n: int): 
    return -n * (n + 1) * (2 + n - 3*n**2) // 12

if __name__ == "__main__":
    n = 100
    print(f"The difference between the sum of the squares of the first {n} natural numbers and the square of the sum is {my_sum(n)}.")