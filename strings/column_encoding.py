"""
    Spreadsheet columns are identified by 'A', 'B', 'C'.....'Z','AA'....'ZZ','AAA'......'ZZZ'
    Implement a function that converts a spreadsheet column id to the corresponding
    integer, with "A' corresponding to 1
    "D" - 4
    'AA" - 702
"""
import functools


def column_encoding(s: str)-> int:
    """
        There are 26 letters in the alphabet
        AA - A(26 ** 1) + A(26 ** 0) = 26 + 1 = 27
        This is a base 26 problem.
        Time Complexity - O(n)
        Space Complexity - O(1)
    """
    result = 0
    for c in s:
        result = result * 26 + ord(c) - ord('A') + 1
    return result


def column_encoding_fp(s: str)-> int:
    """
        There are 26 letters in the alphabet
        AA - A(26 ** 1) + A(26 ** 0) = 26 + 1 = 27
        This is a base 26 problem.
        Time Complexity - O(n)
        Space Complexity - O(1)
    """
    return functools.reduce(
        lambda result, c: result * 26 + ord(c) - ord('A') + 1,
        s, 0)


r = column_encoding_fp('A')
print(r)
r = column_encoding('AA')
print(r)
r = column_encoding_fp('ZZ')
print(r)


