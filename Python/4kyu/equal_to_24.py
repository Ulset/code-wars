"""
https://www.codewars.com/kata/574be65a974b95eaf40008da/python
Task
A game I played when I was young: Draw 4 cards from playing cards, use + - * / and () to make the final results equal to 24.

You will coding in function equalTo24. Function accept 4 parameters a b c d(4 cards), value range is 1-13.

The result is a string such as "2*2*2*3" ,(4+2)*(5-1); If it is not possible to calculate the 24, please return "It's not possible!"

All four cards are to be used, only use three or two cards are incorrect; Use a card twice or more is incorrect too.

You just need to return one correct solution, don't need to find out all the possibilities.
"""

import itertools

paranthese_options = [
    "{a} {a_sign} {b} {b_sign} {c} {c_sign} {d}",
    "({a} {a_sign} {b}) {b_sign} {c} {c_sign} {d}",
    "{a} {a_sign} ({b} {b_sign} {c} {c_sign} {d})",
    "({a} {a_sign} {b}) {b_sign} ({c} {c_sign} {d})"
]


def equal_to_24(a, b, c, d):
    number_combinations = itertools.permutations([a, b, c, d])
    for number_combo in number_combinations:
        a_num, b_num, c_num, d_num = number_combo
        sign_combinations = itertools.product(["+", "-", "/", "*"], repeat=3)
        for sign_combo in sign_combinations:
            a_sign, b_sign, c_sign = sign_combo
            for parantese_opt in paranthese_options:
                eval_test = parantese_opt.format(
                    a=a_num,
                    a_sign=a_sign,
                    b=b_num,
                    b_sign=b_sign,
                    c=c_num,
                    c_sign=c_sign,
                    d=d_num
                )
                try:
                    value = eval(eval_test)
                except ZeroDivisionError:
                    continue

                if value == 24:
                    return eval_test

    return "It's not possible!"
