from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        nums.sort()
        _len = len(nums) - 1
        _count = len(nums)
        for i in range(0, len(nums)):
            if nums[i] == val:
                if nums[_len] == val:
                    nums[_len] = '_'
                    nums[i] = '_'
                else:
                    nums[i] = nums[_len]
                    nums[_len] = '_'
                _len = _len - 1
        print(nums , '->', _count )
        return _count


service = Solution()
service.removeElement([2, 2, 2, 2], 2)
service.removeElement([2, 3, 2, 6], 2)
service.removeElement([1, 2, 3, 4], 3)
service.removeElement([1, 1, 1,1], 3)
service.removeElement([1, 2, 3,4,5,6], 4)
service.removeElement([0,1,2,2,3,0,4,2], 2)  #[0,1,4,0,3]  4