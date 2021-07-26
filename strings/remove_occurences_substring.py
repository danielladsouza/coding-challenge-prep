# L.C. 1910 Remove All Occurrences of a Substring

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
            s = "daabcbaabcbc", part = "abc"
        """
        found_idx = s.find(part)
        while (found_idx != -1):
            s = s[:found_idx] + s[found_idx + len(part):]
            found_idx = s.find(part)

        return s