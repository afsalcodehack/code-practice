import math
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        res = float("inf")

        while l < r:

            mid = (r + l) // 2

            res = min(res, nums[mid])

            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1

        return min(res, nums[l])


driver = Solution()
print(driver.findMin([3, 4, 5, 1, 2]))
print(driver.findMin([4, 5, 6, 0, 1, 2]))
print(driver.findMin([11, 13, 15, 17]))
