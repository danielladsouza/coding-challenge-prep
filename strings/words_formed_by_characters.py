"""
    L.C. 1160 - Find Words That Can Be Formed by Characters
    Naming convention - camelCase for variables, class instance methods
    Pascal case for classes
    Prefix the name of the class with the name of the module (namespace)
    Use descriptive names rather than single letter names

    Input: words = ["cat","bt","hat","tree"], chars = "atach"

    chars is the longer string
"""

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        """
            T.C. O(Nd) N - count of words
                       d - average length of each word (We are iterating over a max of 26 letters)
                       In the worst case d is 26
            T.C. O(N)

            S.C. O(1) - max number of characters is 26, space is fixed
        """
        charCount = collections.Counter(chars)
        result = 0

        for word in words:
            wordChars = Counter(word)

            for letter, count in wordChars.items():
                # We do not have enough characters in the main string "chars"
                if charCount[letter] < count:
                    break
            else:
                result += len(word)

        return result
