"""
Write a function that, given a string of text (possibly with punctuation and line-breaks),
returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
"""
import re


def top_3_words(text):
    text_split = re.sub(r"[^a-zA-Z']", " ", text.lower()).split(" ")  # Remove everything thats not characters or apostrophes, convert to lowercase as requested
    text_split = list(filter(lambda x: x.count("'") != len(x) and x, text_split))  # Remove entries with only apostrophes or whitespace
    word_count = {word: text_split.count(word) for word in text_split}
    return [x[0] for x in sorted(word_count.items(), key=lambda t: t[1], reverse=True)][0:3]  # Return top 3 words based on word count


print(top_3_words("''''   $ ##"))
print(top_3_words("test test test a ting ting"))
print(top_3_words("b c c c d d d d d d d "))
