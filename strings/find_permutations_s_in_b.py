"""
    HackerRank - https://www.youtube.com/watch?v=84UYVCluClQ&feature=youtu.be
    Find all permutations of s within b
    e.g. s xacxsaa
         b fxaazxacaaxzoecazxaxaz

"""

from collections import Counter
from typing import List


def find_all_permutations(s: str, b:str) -> List[str]:
    """
    1. Use a generator and a sliding window to parse through strings in b
    # in O(B) time

    # Use the concept of anagram . Counter for s
    # Compare two counters if there is a match , we have a valid permutation.
    """
    window_size = len(s)
    result = []

    d = Counter(s)
    g = (b[i:i+window_size] for i in range(0, len(b) - window_size -1))
    for y in g:
        c = Counter(y)
        if c == d:
            result.append(y)
    return result


assert(len(find_all_permutations('elvis', 'elvisliveselvisliveselvislive'))
       == 9)

