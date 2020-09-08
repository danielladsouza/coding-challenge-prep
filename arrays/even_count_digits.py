from typing import List

"""Runtime: 56 ms, faster than 72.29% of Python3 online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 14.1 MB, less than 10.35% of Python3 online submissions for Find Numbers with Even Number of Digits.
Time Complexity
Space Complexity
"""
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        s = ""
        even_count = 0
        for n in nums:
            s = str(n)
            if len(s) % 2 == 0:
                even_count += 1
        return even_count

"""
Runtime: 100 ms, faster than 11.16% of Python3 online submissions for Find Numbers with Even Number of Digits.
Memory Usage: 13.7 MB, less than 93.61% of Python3 online submissions for Find Numbers with Even Number of Digits.
Time Complexity
Space Complexity
"""

class Solution1:
    def findNumbers(self, nums: List[int]) -> int:
        s = ""
        even_count = 0
        for n in nums:
            count = 0
            while (n):
                n = int(n / 10)
                count +=1
            if count % 2 == 0:
                even_count += 1
        return even_count