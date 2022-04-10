"""
Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...


Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.
"""


def series_sum(n):
    divide = 1
    output = 0.00
    for _ in range(n):
        output += 1 / divide
        divide += 3
    return "{:.2f}".format(output)


print(series_sum(15))
