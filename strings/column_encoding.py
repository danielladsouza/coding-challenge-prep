"""
    Spreadsheet columns are identified by 'A', 'B', 'C'.....'Z','AA'....'ZZ','AAA'......'ZZZ'
    Implement a function that converts a spreadsheet column id to the corresponding
    integer, with "A' corresponding to 1
    "D" - 4
    'AA" - 702
"""
import string


def column_encoding(s: str)-> int:
    """
        There are 26 letters in the alphabet
        AA - A(26 ** 1) + A(26 ** 0) = 26 + 1 = 27
        This is a base 26 problem.
        Time Complexity - O(n)
        Space Complexity - O(1)
    """
    alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = 0
    for c in s:
        result = result * 26 + alphabets.index(c) + 1
    return result


r = column_encoding('A')
print(r)
r = column_encoding('AA')
print(r)
r = column_encoding('ZZ')
print(r)


