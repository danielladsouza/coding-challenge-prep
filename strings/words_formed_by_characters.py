"""
    L.C. 1160 - Find Words That Can Be Formed by Characters
"""
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """
            T.C. O(Nd) N - count of words
                       d - length of each word

            S.C. O(d) - Counter of chars in w
        """
        charCount = Counter(chars)
        result = 0

        for w in words:
            wCount = Counter(w)

            for key, value in wCount.items():
                if charCount[key] < value:
                    break
            else:
                result += len(w)

        return result
