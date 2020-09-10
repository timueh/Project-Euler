"""
# ProjectEuler.net - Problem 3

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def find_largest_palindrome():
    palindromes = []
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            prod = i * j

            if str(prod) == str(prod)[::-1]:
                palindromes.append(prod)

    return max(palindromes)


if __name__ == "__main__":
    print(find_largest_palindrome())