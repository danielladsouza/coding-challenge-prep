from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        i = 0
        three_sum_list = []
        while i < len(nums) - 2:
            a = nums[i]
            if i > 0 and a == nums[i-1]:
                i += 1
                continue
            target = 0 - a
            three_sum_helper_list = self.three_sum_helper(nums[i+1:], target, a)
            three_sum_list += three_sum_helper_list
            i += 1
        return three_sum_list
        
    def three_sum_helper(self, numbers: List[int], target: int, a:int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        result = []
        while (l < r):
            b = numbers[l]
            if l > 0 and b == numbers[l-1]:
                l += 1
                continue
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                result.append([a, numbers[l], numbers[r]])
                l += 1
                r -= 1

        return result

s = Solution()
#result = s.threeSum([-1,1,0,])
#result = s.threeSum([-1,1,0,2,-2,-1])
result = s.threeSum([9,-15,6,6,10,-2,8,8,0,-6,-4,-2,14,-6,-14,-2,12,5,-2,-8,13,13,-10,4,-6,8,6,-15,-5,11,-15,11,3,-2,-6,-10,11,-12,13,-12,-11,-5,2,10,-4,-5,-15,-7,7,-2,0,5,-11,-3,-13,-10,-9,0,-10,-7,-12,12,-11,7,-5,-1,12,-8,-6,3,-13,-10,5,-4,-14,-14,6,8,-14,-9,-8,-7,3,-4,6,5,1,12,-9,6,-10,-6,-5,-14,-14,5,-8,6,4,1])
#result = s.twoSum([-1,1,0], 1)
print(result)