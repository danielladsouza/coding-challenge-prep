"""
    convert_base.py
    Perform base conversion. The input is a string, an integer b1, and another
    integer b2
"""
import string


def convert_base(s: str, b1: int, b2: int) -> str:
    # 1. Convert the str base b1 to an integer base 10. This enables us to
    # do multiplication / addition operations
    result_as_int, is_negative = 0, s[0] == '-'
    for c in s[is_negative:]:
        # Since the string will contain Uppercase letters ['A', 'B'....'F']
        # we need to convert them to lowercase so that we get the correct index
        result_as_int = result_as_int * b1 + string.hexdigits.index(c.lower())

    # 2. Convert the int result to a string base b2
    def convert_to_base(n : int, b2: int) -> str:
        result_b2 = []
        # Check for case when result_as_int is 0
        if n == 0:
            return '0'
        while n:
            result_b2.append(string.hexdigits[n % b2].upper())
            n = n // b2

        # join takes an iterable as an argument
        return ''.join(reversed(result_b2))

    return ('-' if is_negative else '') + convert_to_base(result_as_int, b2)


r = convert_base("-615", 7, 13)
print(r)

r = convert_base("615", 7, 13)
print(r)

r = convert_base("0", 7, 13)
print(r)

