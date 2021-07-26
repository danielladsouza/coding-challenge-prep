# L.C. 1920. Build Array from Permutation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i, n in enumerate(nums):
            ans.append(nums[n])

        return ans