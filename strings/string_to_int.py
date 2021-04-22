"""
    Implement a method that takes a string representing and integer and return
    the corresponding integer
    Code should handle negative values
"""


def string_to_int(s:str) -> int:
    """ Time complexity O(N)
        Space complexity O(1)"""
    # Parse the string character by character. Build up the corresponding int
    # Use the ord, chr for conversion.
    lookup = dict((chr(ord('0') + i), i) for i in range(10))
    # dictionary - '0': 0...'9':9
    result, negative = 0, False

    for c in s:
        if c == '-':
            negative = True
            continue

        result = lookup[c] + result * 10

    if negative and result:
        result = -result

    return result


r = string_to_int("123")
print(r)
r = string_to_int("000")
print(r)

r = string_to_int("-123")
print(r)
r = string_to_int("-000")
print(r)