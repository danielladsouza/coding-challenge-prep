# 916. Word Subsets https://leetcode.com/problems/word-subsets/

from collections import Counter
from typing import List

"""
O(A + B) time
O(1) space
"""

def getRequiredCharCounts(B: List[str]):
    """
        Returns the minimum count of characters a string should contain to be considered universal
    """
    reqdCharCounts = Counter('')
    for b in B:
        bCounts = Counter(b)
        for letter in bCounts:
            reqdCharCounts[letter] = max(reqdCharCounts[letter], bCounts[letter])
    return reqdCharCounts


def findUniversalStrings(A, reqdCharCounts):
    """
        Returns the subset of strings in A that meet the count of characters specified
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

def wordSubsets(A: List[str], B: List[str]) -> List[str]:
    """
    >>> wordSubsets(["amazon","apple","facebook","google","leetcode"], ["l","e"])
    ['apple', 'google', 'leetcode']
    >>> wordSubsets(["amazon","apple","facebook","google","googllle","leetcode"], ["lll","e"])
    ['googllle']
    """
    reqdCharCounts = getRequiredCharCounts(B)
    results = findUniversalStrings(A, reqdCharCounts)
    return results
