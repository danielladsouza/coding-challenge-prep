# L.C. 49 - Group Anangrams

from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # T.C O(MN)  -- M number of characters in each word, N number of words
        # S.C. O(N) -- Instead of a single list, we now have a list of lists
        #              The total number of words stays at N
        def signature(word):
            # count numbers of characters in word
            # We know that there are 26 lowercase English letters
            # Each index to represent a letter from the alphabet
            count = [0]*26
            for char in word:
                count[ord(char) - ord("a")] += 1
                # This becomes our hashing function ord(char) - ord("a")
            return str(count)   # string representation of the Object list

        # hashmap of number counts
        anagrams = defaultdict(list)
        for word in strs:
            anagrams[signature(word)].append(word)

        return anagrams.values()

