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

s = Solution()
result = s.permute_elements_array_storage([2,0,1,3], ['a', 'b', 'c', 'd'])
print(result)






