from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = [ ]
        for i , v in enumerate(nums):
            idx = abs(v) - 1
            nums[idx] = abs(nums[idx]) * -1
        for i, v in enumerate(nums):
            if v > 0:
                res.append(i+1)
        return res



driver = Solution()
driver.findDisappearedNumbers([4,3,2,7,8,2,3,1])
driver.findDisappearedNumbers([1,1])