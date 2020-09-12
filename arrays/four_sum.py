from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int):
        if len(nums) < 4:
            return []
        
        nums.sort()
        four_sum_list = []
        i = 0

        while i < len(nums) - 3:
            a = nums[i]
            if i > 0 and a == nums[i-1]:
                i += 1
                continue
            four_sum_helper_list = self.four_sum_helper(nums[i+1:], target - a, a)
            four_sum_list += four_sum_helper_list
            i += 1
        return four_sum_list

    def four_sum_helper(self, nums: List[int], target: int, a: int) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        i = 0
        three_sum_list = []
        while i < len(nums) - 2:
            b = nums[i]
            if i > 0 and b == nums[i-1]:
                i += 1
                continue
    
            three_sum_helper_list = self.three_sum_helper(nums[i+1:], target - b, a, b)
            three_sum_list += three_sum_helper_list
            i += 1
        return three_sum_list
        
    def three_sum_helper(self, numbers: List[int], target: int, a:int, b:int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        result = []
        while (l < r):
            c = numbers[l]
            if l > 0 and c == numbers[l-1]:
                l += 1
                continue
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                result.append([a, b, numbers[l], numbers[r]])
                l += 1
                r -= 1

        return result


s = Solution()
#result = s.fourSum([1, 0, -1, 0], 0)
result = s.fourSum([1, 0, -1, 0, -2, 2], 0)
print(result)