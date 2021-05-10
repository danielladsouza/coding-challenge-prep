"""
    Given an integer (negative, 0, positive value)
    returen the equivalent binary value as a string
"""
import string


def convert_to_binary(n: int) -> str:
    """
        Edge cases
            0, -ve, +ve
        Use an array to collect the bit values and append them, instead
        of manipulating strings (strings carry the overhead of allocation of a
        new string every time it is modified as strings are immutable)
        Arrays on the other head a mutable, but carry the overhead of movement
        of existing elements if elements are prepended to the array as opposed
        to appended.
        Time Complexity - O(K) - k is the number of bits in the binary equivalent
        Space Complexity - O(k) - Length of the resulting string
    """
    result = []
    is_negative = n < 0
    if is_negative:
        n = -n

    if not n:
        result = '0'

    while n:
        # Faster O(1) - String array lookup
        result.append(string.digits[n % 2])
        n = n // 2

    # Avoid call to a function , map
    # return ('-' if is_negative else '') + ''.join(map(str, reversed(result)))
    return ('-' if is_negative else '') + ''.join(reversed(result))


print(convert_to_binary(0))
print(convert_to_binary(8))
print(convert_to_binary(-8))
