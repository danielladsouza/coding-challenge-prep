# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
# Find the peak element index

from typing import List

class Solution:
    def __init__(self):
        # Instance level variable 
        self.peak_index = None
        
    def find_peak_element(self, mountain_arr: List[int]) -> int:
        # Find the inflection point - index i .. mountain_arr[i-1] < mountain_arr[i] 
        # mountain_arr[i] > mountain_arr[i+1]

        def binarysearch_peak_index(l : int, r : int) -> (int, int):
            mid = int((l + r) / 2)
            if mountain_arr[mid-1] < mountain_arr[mid] and mountain_arr[mid] > mountain_arr[mid + 1]:
                    self.peak_index = mid
                    return
            
            # on the rise
            if mountain_arr[mid-1] < mountain_arr[mid]:
                binarysearch_peak_index(mid+1, r)
            else:
                binarysearch_peak_index(l, mid - 1)
            
        binarysearch_peak_index(0, len(mountain_arr) - 1) 
        return self.peak_index

                
s = Solution()
#index = s.find_peak_element([1,2,3,4,5,6,8,7,5,4,3,1])
index = s.find_peak_element([-8, -6, -5, -4, -3, -2, -1, 5, 4, 3, 1])
print(index)