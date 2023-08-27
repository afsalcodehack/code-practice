from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        _len = len(nums) - 1
        _count = 0
        for i in range(0, len(nums)):
            if nums[i] == val:
                if nums[_len] == val and nums[_len] != '_':
                    nums[_len] = '_'
                    nums[i] = '_'
                else:
                    nums[i] = nums[_len]
                    nums[_len] = '_'
                _len = _len - 1
            if nums[i] != '_':
                _count = _count + 1
        print(nums , '->', _count )
        return _count
    
    def removeElement2(self, nums: List[int], val: int) -> int:
        _index = 0
        for i in nums:
            if i != val:
                nums[_index] = i
                _index = _index + 1
        print(_index)
        return _index;


service = Solution()
service.removeElement([2, 2, 2, 2], 2) #0
service.removeElement([2, 3, 2, 6], 2) #2
service.removeElement([1, 2, 3, 4], 3) #3
service.removeElement([1, 1, 1,1], 3)#4
service.removeElement([1, 2, 3,4,5,6], 4) #5
service.removeElement([0,1,2,2,3,0,4,2], 2)  #5
print('-----------------------------------------')
service = Solution()
service.removeElement2([2, 2, 2, 2], 2) #0
service.removeElement2([2, 3, 2, 6], 2) #2
service.removeElement2([1, 2, 3, 4], 3) #3
service.removeElement2([1, 1, 1,1], 3)#4
service.removeElement2([1, 2, 3,4,5,6], 4) #5
service.removeElement2([0,1,2,2,3,0,4,2], 2)  #5