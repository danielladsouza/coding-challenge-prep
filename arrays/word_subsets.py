# 916. Word Subsets https://leetcode.com/problems/word-subsets/

from collections import Counter
from typing import List


"""
O(A + B) time
O(1) space
"""
class Solution:
    def getRequiredCharCounts(self, B: List[str]):
        """
            Returns the minimum count of characters a string should contain to be considered universal
        """
        reqdCharCounts = Counter('')
        for b in B:
            bCounts = Counter(b)
            for letter in bCounts:
                reqdCharCounts[letter] = max(reqdCharCounts[letter], bCounts[letter])
        return reqdCharCounts

    
    def findUniversalStrings(self, A, reqdCharCounts):
        """
            Returns the subset of strings in A who meet the count of characters specified
        """
        results = []
        for a in A:
            aCounts = Counter(a)
            for letter in reqdCharCounts:
                if aCounts[letter] < reqdCharCounts[letter]:
                    break
            else:
                results.append(a)
        return results

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        reqdCharCounts = self.getRequiredCharCounts(B)
        results = self.findUniversalStrings(A, reqdCharCounts)
        return results
