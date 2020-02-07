"""
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
"""

def duplicate_encode(word):
    multi = []
    tested = []
    for i in word.lower():
        if i in tested:
            multi.append(i)
        else:
            tested.append(i)
    output = ""
    for i in word.lower():
        if i in multi:
            output += ")"
        else:
            output += "("
    return output
