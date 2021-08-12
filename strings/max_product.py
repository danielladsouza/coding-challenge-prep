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

            Brute Force approach
            1000 words each upto 1000 in length
            TC O(N**2)
            SC O(N)

        """
        max_product = 0
        words_counter = [None] * len(words)
        for i, w in enumerate(words):
            words_counter[i] = Counter(w)

        for i in range(len(words_counter) - 1):
            for j in range(i + 1, len(words_counter)):
                for key in words_counter[i]:  # We have to iterate over each of the key letters
                    if key in words_counter[j]:
                        break
                else:
                    max_product = max(max_product,
                                      len(words[i]) * len(words[j]))
        return max_product

    def maxProduct(self, words: List[str]) -> int:
        """
            1. Find out words that do not share common letters
            word into a Counter for comparison
            2. T.C. O(N**2)  - Brute Force approach

            Iterate over the words comparing bitmasks for word[i] with word[j]. If nothing in common,
            calculate the product. This saves us from having to compare each individual character in the word
            THe length of each word can extend upto 1000 characters, even using a dictionary we would need to
            aggregate the data and then compare.

            Track the max_product

            Brute Force approach
            1000 words each upto 1000 in length
            TC O(N**2)
            SC O(N)

        """
        def build_bitmask(word: str) -> int:
            bitmask = 0
            for char in word:
                bitmask = bitmask | (1 << (ord(char) - ord('a')))

            return bitmask

        max_product = 0
        words_bitmask = list(map(build_bitmask, words))

        for i in range(len(words_bitmask) - 1):
            for j in range(i + 1, len(words_bitmask)):
                if words_bitmask[i] & words_bitmask[j] == 0:
                    max_product = max(max_product,
                                      len(words[i]) * len(words[j]))
        return max_product
