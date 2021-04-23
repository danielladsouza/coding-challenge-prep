"""
    convert_base.py
    Perform base conversion. The input is a string, an integer b1, and another
    integer b2
"""
import string


def convert_base(s: str, b1: int, b2: int) -> str:
    # 1. Convert the str base b1 to an integer base 10. This enables us to
    # do multiplication / addition operations
    result_b1, is_negative = 0, s[0] == '-'
    for c in s[s[0] == '-':]:
        result_b1 = result_b1 * b1 + string.hexdigits.index(c)

    # 2. Convert the int result to a string base b2
    result_b2 = []
    while result_b1:
        result_b2.append(string.hexdigits[result_b1 % b2].upper())
        result_b1 = result_b1 // b2

    return ('-' if is_negative else '') + ''.join(reversed(result_b2))


r = convert_base("615", 7, 13)
print(r)


