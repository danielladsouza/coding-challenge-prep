"""
    L.C. 953 - Verifying an Alien Dictionary
    In an alien language, surprisingly they also use english lowercase letters,
     but possibly in a different order. The order of the alphabet is some
    permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of
    the alphabet, return true if and only if the given words are sorted
    lexicographicaly in this alien language.

    How is this true
    ["kuvp","q"]
    "ngxlkthsjuoqcpavbfdermiywz"

    The first three characters "app" match, and the second string is shorter
    (in size.) According to lexicographical rules "apple" > "app",
    because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

"""
from typing import List


class Solution:
    def isAlienSorted_1(self, words: List[str], order: str) -> bool:
        if len(words) < 2:
            return True

        # It is incorrect to expect the prior string to be shorter in length
        # than the current string.
        # " "kuvp" < "l" "

        def strings_sorted(s1, s2):
            """
                returns True if s1 comes before s2 in the specified lexicographical order
            """

            for i in range(min(len(s1), len(s2))):
                if order.index(s1[i]) < order.index(s2[i]):
                    break

                if order.index(s1[i]) > order.index(s2[i]):
                    return False

                # If equal we just continue

            # "apple", "app"
            if s1[i] == s2[i] and len(s1) > len(s2):
                return False

            return True

        for i in range(1, len(words)):
            if not strings_sorted(words[i - 1], words[i]):
                return False

        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """
            T.C. O(MN)
            M - Number of words
            N - maximum length of a word in words
        """

        if len(words) < 2:
            return True

        order_lookup = dict((c, i) for i, c in enumerate(order))
        prev = words[0]
        match_length = 0
        for current in words[1:]:
            for pair in zip(prev, current):
                if order_lookup[pair[0]] > order_lookup[pair[1]]:
                    return False
                if order_lookup[pair[0]] < order_lookup[pair[1]]:
                    break
                match_length += 1
            # Check for end of zip due to unequal lengths of strings
            if len(current) != len(prev):
                if match_length == len(current):
                    return False
            prev = current
        return True


"""
    Test Cases
    words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    True
    words = ["hello", "hellocode"],  order = "hlabcdefgijkmnopqrstuvwxyz"
    True
    words = ["hello", "hellocode"],  order = "hlabcdefgijkmnopqrstuvwxyz"
    True
    
    words = ["hello", "h"],  order = "hlabcdefgijkmnopqrstuvwxyz"
    True
    
    
"hlabcdefgijkmnopqrstuvwxyz"
["word","world","row"]
"worldabcefghijkmnpqstuvxyz"
["apple","app"]
"abcdefghijklmnopqrstuvwxyz"

"""