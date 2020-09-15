from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        
        def helper(target: int, i: int, sub_list: List[int]):
            if target == 0:
                # Combine/Conquer
                result.append(sub_list)
                return
                
            if target < 0 or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if target < candidates[j]:
                    break
                  
                # Divide
                helper(target - candidates[j], j, sub_list + [candidates[j]])
                
        helper(target, 0, [])
        return result


s = Solution()
result = s.combinationSum([2,3,6,7], 7)
#result = s.combinationSum([2,3,5], 8)
print(result)
