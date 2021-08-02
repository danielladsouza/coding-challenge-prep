# L.C. 748 Shortest Completing Word

import string, copy
from collections import defaultdict


class Solution:
    def shortestCompletingWord(self, licensePlate: str,
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