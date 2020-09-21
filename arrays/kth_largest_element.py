from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        kth_largest_list =  heapq.nlargest(k, nums)
        # kth largest element in the list
        return kth_largest_list[-1]


s = Solution()
res = s.findKthLargest([3,2,1,5,6,4], 3)
print(res)
