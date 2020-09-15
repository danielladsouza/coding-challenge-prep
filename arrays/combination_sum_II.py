from typing import List

# Backtracking
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        # This is so that we know when to terminate..
        # consider the smaller numbers first towards building the sub list for the target.
        candidates.sort()
       
        def helper(target, i, sub_list):
            if target == 0:
                result.append(sub_list)  
                return
            
            if target < 0 or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
            
                # looking for duplicates in the sub sequence candidates[i:]
                # Hence look for index > i
                if j > i and candidates[j] == candidates[j-1]:
                    continue
            
                if target < candidates[j]:
                    break
                # We do not want to reuse the same element twice
                helper(target - candidates[j], j+1, sub_list + [candidates[j]])
                  
            
        helper(target, 0, [])
        return result

s = Solution()
result = s.combinationSum2([10,1,2,7,6,1,5], 8)
"""[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""
print(result)