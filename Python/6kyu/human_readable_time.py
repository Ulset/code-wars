"""
Write a function, which takes a non-negative integer (seconds) as input and
returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""


def make_readable(seconds):
    hours = str(seconds // (60 * 60)).rjust(2, "0")
    minutes = str((seconds % 3600) // 60).rjust(2, "0")
    seconds = str((seconds % 3600) % 60).rjust(2, "0")
    return f"{hours}:{minutes}:{seconds}"


print(make_readable((60 * 60 * 4) + 120 + 3))
