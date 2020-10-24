# https://leetcode.com/problems/daily-temperatures/
"""
How many days you would have to wait until a warmer temperature

There are two basic ideas here: work backwards and use a stack. We keep a stack of temperatures and their index, in increasing order. 
Every time we see a new temperature we pop items off the stack until we see a bigger temperature. The answer for the current temperature 
is then the index of the top of the stack minus the current index. If the stack is empty, then the answer is -1. We then add the current 
temperature and its index to the stack, and move onto the next temperature.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].


(This can be simplified by just storing the index in the stack and looking up the temperature.)

The stack starts off empty and we start from the last temperature and work backwards.

O(n) time
O(n) space


Explanation of stack..

"""
from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        results = [0] * len(T)
        seenTemps = []
        for i in reversed(range(len(T))):
            if seenTemps:
                while (seenTemps and T[i] >= T[seenTemps[-1]]):
                    seenTemps.pop()
                if seenTemps:
                    results[i] = seenTemps[-1] - i
            seenTemps.append(i)
        return results

"""
T = [73, 74, 75]    results = [0,0,0]
seenTemps[]
i
seenTemps[-1]  Top of the stack

    seenTemps    results
2      2           0
1      2,1         1 
0      2,1,0       1

"""
s = Solution()
result = s.dailyTemperatures([73, 74, 75])
print(result)