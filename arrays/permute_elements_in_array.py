# EPI 5.10 - Permute the elements of an array
from typing import List

# perms [2,0,1,3]
# s ['a', 'b', 'c', 'd']

class Solution:
    """ Uses additional storage"""
    """ Time Complexity O(n), Space Complexity O(n)"""
    def permute_elements_array_storage(self, perms : List[int], s : List[str] ) -> str:
        B = s.copy()
        for i in range(len(s)):
            B[perms[i]] = s[i]

        return B

    """ Does not use additional storage, however does update the perms array"""
    """ Time Complexity O(n), Space Complexity O(n) """
    def permute_elements_array(self, perms : List[int], s : List[str]) -> str:
        # [c,b,a,d] [1,0, 2, 3]
        # [b,c,a,d] [0,1,2,3]
        for i in range(len(s)):
            while perms[i] != i:
                s[i], s[perms[i]] = s[perms[i]], s[i]
                perms[i], perms[perms[i]] = perms[perms[i]], perms[i]

        return s

s = Solution()
result = s.permute_elements_array_storage([2,0,1,3], ['a', 'b', 'c', 'd'])
print(result)