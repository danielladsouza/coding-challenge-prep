# L.C. 318 - Maximum Product of Word Lengths

from collections import Counter


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
            1. Find out words that do not share common letters
            word into a Counter for comparison
            2. T.C. O(N**2)  - Brute Force approach

            Iterate over the words comparing word[i] with word[j]. If nothing in common,
            calculat the product
            Track the max_product

        """
        max_product = 0
        words_counter = [None] * len(words)
        for i, w in enumerate(words):
            words_counter[i] = Counter(w)

        for i in range(len(words_counter) - 1):
            for j in range(i + 1, len(words_counter)):
                for key in words_counter[i]:
                    if key in words_counter[j]:
                        break
                else:
                    max_product = max(max_product,
                                      len(words[i]) * len(words[j]))
        return max_product