"""
Write an algorithm that takes an array and moves all of
the zeros to the end, preserving the order of the other elements.
"""


def move_zeros(liste: list):
    zero_counter = 0
    output = []
    for i, el in enumerate(liste):
        if el == 0:
            zero_counter += 1
        else:
            output.append(el)
    output = output + [0 for _ in range(zero_counter)]
    return output


def move_zeros_but_cool(array: list):
    zeros = [x for x in array if x == 0]
    not_zeros = [x for x in array if x != 0]
    return not_zeros + zeros


print("Output: ", move_zeros_but_cool([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]))
print("Correct: ", [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
