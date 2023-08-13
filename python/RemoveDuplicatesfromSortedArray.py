from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        _len = len(nums) - 1
        i = 0
        while i <= _len:
            if i > 0:
                if nums[i - 1] == nums[i]:
                    del nums[i]
                    _len -= 1
                    i -= 1
            i += 1

        print(nums)


service = Solution()
service.removeDuplicates([0, 0, 0, 1 ,1])
