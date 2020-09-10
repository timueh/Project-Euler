"""
# ProjectEuler.net - Problem 1

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def find_multiples(number, div):
    max_multiplier = divmod(number-1, div)[0]
    multiples = set(range(div, max_multiplier*div+1, div))
    return multiples


def find_multiples_and_sum(number, divs):
    multiples = []
    for div in divs:
        m = find_multiples(number, div)
        multiples.append(m)
    return sum(set.union(*multiples))


if __name__ == "__main__":
    m = find_multiples_and_sum(1000, [3, 5])
    print(f"The sum is {m}.")