from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i , v in enumerate(nums):
            left_sum += v
            if (left_sum - v) == (total - left_sum):
                return i
        return -1


driver = Solution()

print(driver.pivotIndex([1, 7, 3, 6, 5, 6]), 3)
print(driver.pivotIndex([1, 1, 1, 4, 3]), 3)
print(driver.pivotIndex([1, 1, 1, 1, 1, 4, 5]), 5)
print(driver.pivotIndex([2, 1, -1]), 0)
print(driver.pivotIndex([1, 2, 3]), -1)
print(driver.pivotIndex([-1,-1,-1,-1,-1,0]), 2)
