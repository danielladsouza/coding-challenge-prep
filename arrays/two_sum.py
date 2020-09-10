from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        result = []
        
        for i, v in enumerate(nums):
            if v in comp:
                result.append(comp[v])
                result.append(i)
                break
            comp[target - v] = i
            
        return result


s = Solution()
print(s.twoSum([-3,4,3,9,0], 0))

