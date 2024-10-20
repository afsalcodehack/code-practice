from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        _max = 0
        for i in range(len(nums), 0):
            if i != 0:
                nums[i] += nums[i - 1]

                if ((i + 1) / 2) == nums[i]:
                    _max = i + 1
        return _max


driver = Solution()
print(driver.findMaxLength([0, 1, 0]))
