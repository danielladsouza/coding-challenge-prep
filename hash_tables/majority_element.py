# LC 169. Majority Element https://leetcode.com/problems/majority-element/

from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        max_freq = 0
        freq_counter = defaultdict(int)
        
        for n in nums:
            freq_counter[n] += 1
            
            if freq_counter[n] > max_freq:
                max_freq = freq_counter[n]
                result = n
        return result
            