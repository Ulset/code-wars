import math

"""
https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/train/python
The prime numbers are not regularly spaced. For example from 2 to 3 the gap is 1. From 3 to 5 the gap is 2. From 7 to 11 it is 4. Between 2 and 50 we have the following pairs 
of 2-gaps primes: 3-5, 5-7, 11-13, 17-19, 29-31, 41-43 

A prime gap of length n is a run of n-1 consecutive composite numbers between two successive primes (see: https://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g (integer >= 2) which indicates the gap we are looking for

m (integer > 2) which gives the start of the search (m inclusive)

n (integer >= m) which gives the end of the search (n inclusive)

n won't go beyond 1100000.

In the example above gap(2, 3, 50) will return [3, 5] which is the first pair between 3 and 50 with a 2-gap.

So this function should return the first pair of two prime numbers spaced with a gap of g between the limits m, n if these numbers exist otherwise `nil or null or None or 
Nothing (or ... depending on the language). 
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
