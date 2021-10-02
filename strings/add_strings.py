"""
    L.C. 415 - Add Strings
"""
import string

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
            Algorithm
            The numbers could be of length upto 10 ** 4
            11
            129

            We would like to add the least significant digits first
            - Iterate over the strings in reversed order.
            11
            921

            add the digits keeping track of the carryover and the least significant digit of the result
            Note - Use of the reversed iterator instead of reversing the entire string
            Also when we collect the sum of the digits we are storing the characters in a list instead of a string
            concat as strings are immutable.
            Lastly to return the final result we again use the reversed() iterator.

            Notice the use of iterators to be more efficient with space.
            Strings are immutable.
        """
        rev_iter1 = reversed(num1)
        rev_iter2 = reversed(num2)
        carryover = 0

        c1 = next(rev_iter1, None)
        c2 = next(rev_iter2, None)

        rev_result_list = []

        while c1 or c2 or carryover:
            sum = (string.digits.index(c1) if c1 else 0) + (
                string.digits.index(c2) if c2 else 0) + carryover
            carryover = sum // 10   # Quotient
            rev_result_list.append(string.digits[sum % 10])  # Remainder
            c1 = next(rev_iter1, None)
            c2 = next(rev_iter2, None)

        return ''.join(reversed(rev_result_list))


s = Solution()
result = s.addStrings("11", "239")
print(result)