"""
    Implement a method that takes a string representing and integer and return
    the corresponding integer
    Code should handle negative values
"""
import string


def string_to_int(s:str) -> int:
    """ Time complexity O(N)
        Space complexity O(1)"""
    # Parse the string character by character. Build up the corresponding int
    result = 0

    for c in s[s[0] == '-':]:
        result = string.digits.index(c) + result * 10

    return result * (-1 if s[0] == '-' else 1)


r = string_to_int("123")
print(r)
r = string_to_int("000")
print(r)

r = string_to_int("-123")
print(r)
r = string_to_int("-000")
print(r)