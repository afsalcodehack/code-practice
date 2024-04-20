from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum = nums[0]
        max_sum = nums[0]
        j = 1
        while j < len(nums):
            if sum < 0:
                sum = nums[j]
            else:
                sum += nums[j]
            max_sum = max(sum, max_sum)
            j += 1
        print(max_sum)


driver = Solution()
driver.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
driver.maxSubArray([5, 4, -1, 7, 8])
driver.maxSubArray([1])
driver.maxSubArray([-2, 1])
driver.maxSubArray([1, 2])
driver.maxSubArray([1, 2, 0, 0, 4])
driver.maxSubArray([-2, -1, -4])
