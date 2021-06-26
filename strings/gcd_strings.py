# LC 1071 Greatest Common Divisor of Strings

class Solution:
    """
        T.C - O(M/N) - M is the length of the input strings, N is the length of the GCD string  ~ O(M)
        S.C - O(1)
    """
    @staticmethod
    def greatest_common_divisor(a, b):
        while b:
            a = a % b
            a, b = b, a
        return a

    @staticmethod
    def is_factor(s1, s2):
        for i in range(len(s2) // len(s1)):
            if s2[i * len(s1): (i + 1) * len(s1)] != s1:
                return False
        return True

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
            Input: str1 = "ABCABC", str2 = "ABC"
            Output: "ABC"

            Input: str1 = "ABCDEF", str2 = "ABC"
            Output: ""
        """
        # 1. Determine the portion of the string that is the GCD
        l1 = len(str1)
        l2 = len(str2)

        len_gcd = Solution.greatest_common_divisor(l1, l2)
        gcd_str = str1[:len_gcd]

        if (Solution.is_factor(gcd_str, str1) and Solution.is_factor(gcd_str, str2)):
            return gcd_str
        else:
            return ""
