# L.C. 318 - Maximum Product of Word Lengths
"""
    Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters.
    If no such two words exist, return 0.
    Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    Output: 16
    Explanation: The two words can be "abcw", "xtfn".
"""

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

            Bitmasks are useful anytime you need to keep track of which of N items is in a group. the group is represented by a N digit binary number,
            and the ith bit is 1 if the item is present and 0 otherwise. We can therefore see where two groups share items by taking the and of their masks;
            the remaining bits are the shared items. Remember that left shifting by i is an easy way to get the 2^i, the ith digit.
            Once we have the bitmasks the rest of the problem is very basic; as long as the and of the two word bitmasks is 0 then we have a valid pair.

        """
        def build_bitmask(word: str) -> int:
            """
                Build a 26 bit binary number
            """
            bitmask = 0
            for char in word:
                bitmask = bitmask | (1 << (ord(char) - ord('a')))
            return bitmask

        max_product = 0
        bitmask_words = list(map(build_bitmask, words))

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                # Do the comparison using the bitmasked version of the words
                # Nothing in common will yield 0 for an and
                if bitmask_words[i] & bitmask_words[j] == 0:
                    max_product = max(max_product,
                                      len(words[i]) * len(words[j]))
        return max_product