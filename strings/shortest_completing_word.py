# L.C. 748 Shortest Completing Word
import typing
import string, copy
from collections import Counter, defaultdict

class Solution:
    """
    O(n * m) time
    O(1) space
"""
    @staticmethod
    def wordToCounter(word: str) -> Dict:
        'Keeps track of the count of lowercase letters in a string'
        wordCount = defaultdict(int)
        for c in word.lower():
            if c in string.ascii_lowercase:
                wordCount[c] += 1
        return wordCount

    def shortestCompletingWord(self, licensePlate: str,
                               words: List[str]) -> str:
        result = ""

        licenseCount = Solution.wordToCounter(licensePlate)

        for word in words:  # T.C. O(M) M is the number of words
            wordCount = Solution.wordToCounter(
                word)  # T.C. O(N) N is the number of letters in the word

            for letter in string.ascii_lowercase:  # O(26)
                # Think of iterating over the keys (lowercase letters)
                # 26 letters
                if licenseCount[letter] > wordCount[letter]:
                    break
            else:  # Good use of for .. else  we have successfully compared all the required letter counts
                # word is a possible candidate
                # order is being maintained by the word list
                # select the shortest of the candidates - len
                if not result or len(result) > len(word):
                    result = word
        return result

    def shortestCompletingWord_2(self, licensePlate: str,
                               words: List[str]) -> str:
        result = ""
        licenseCount = collections.Counter(licensePlate.lower()) # 7 max keys

        for word in words: # O(M)
            wordCount = collections.Counter(word.lower())  # 1000 max length of a word O(N)
            for letter in string.ascii_lowercase: # O(26)
                # Think of iterating over the keys (lowercase letters)
                # 26 letters
                if licenseCount[letter] > wordCount[letter]:
                    break
            else:
                # word is a possible candidate
                # order is being maintained by the word list
                # select the shortest of the candidates - len
                if not result or len(result) > len(word):
                    result = word
        return result

    def shortestCompletingWord_1(self, licensePlate: str,
                               words: List[str]) -> str:
        # licensePlate
        # Min, Count of the desired characters
        # Ignore numbers, spaces, case insensitive

        """get_desired_characters()
        Iterate over words and get the candidate completing words
        pick the first of the shortest of the completing words"""

        licensePlateMap = defaultdict(
            int)  # S.C. O(d) - length of the licensePlate string

        licensePlate = licensePlate.lower()  # strings are immutable

        for c in licensePlate:  # T.C. O(d)
            if c in string.ascii_lowercase:
                licensePlateMap[c] += 1

        # 1s3 PSt
        # spst
        # Keep track of the shortest completing word
        result = None

        # Analyze for Time complexity
        # T.C. O(Nd)
        for word in words:  # O(N)
            ref_map = licensePlateMap.copy()  # Shallow copy - no Nested reference types
            for c in word:  # O(d)
                if c in ref_map:
                    ref_map[c] -= 1

            if max(ref_map.values()) > 0:
                continue

            if result == None:
                result = word
            if len(word) < len(result):
                result = word

        return result