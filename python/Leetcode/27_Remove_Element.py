from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        nums.sort()
        _len = len(nums) - 1
        _count = len(nums)
        for i in range(0, len(nums)):
            if nums[i] == val:
                _count = _count - 1
                if nums[_len] == val:
                    nums[_len] = '_'
                    nums[i] = '_'
                else:
                    nums[i] = nums[_len]
                    nums[_len] = '_'
            _len = _len - 1
        print(nums)
        return _count


service = Solution()
print(service.removeElement([2, 3, 2, 6], 2))
print(service.removeElement([2, 2, 2, 2], 2))
print(service.removeElement([1, 2, 3, 4], 3))
print(service.removeElement([1, 1, 1,1], 3))

