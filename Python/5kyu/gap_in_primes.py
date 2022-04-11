import math

"""
Returns two primes with the gap of g
"""


# First thought the primes didnt have to be the next prime in range
def gap_space_allowed(g, m, n):
    primes_in_range = [x for x in range(m, n + 1) if is_prime(x)]
    for prime in primes_in_range:
        for prime_target in primes_in_range:
            if prime_target - prime == g:
                return [prime, prime_target]


# Solution that only gives back primes with gap when they are the next valid prime
def gap(g, m, n):
    first_prime = None
    while m <= n:
        if is_prime(m):
            if first_prime and m - first_prime == g:
                return [first_prime, m]
            else:
                first_prime = m
        m += 1


def is_prime(x):
    return not [y for y in range(2, int(math.sqrt(x) + 1)) if x % y == 0]


print(gap(2, 100, 103))
