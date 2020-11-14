# LC 169. Majority Element https://leetcode.com/problems/majority-element/
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_value = 0
        majority_count = 0
        
        for x in nums:
            if majority_count == 0:
                majority_value = x
                majority_count = 1
            elif majority_value == x:
                majority_count += 1
            else:
                majority_count -= 1
        return majority_value