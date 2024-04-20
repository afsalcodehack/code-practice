from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _max = 0
        _numSet = set(nums)
        for i in _numSet:

            longest = 0

            if (i - 1) not in _numSet:
                while (i + longest) in  _numSet:
                    longest += 1
            _max = max(_max, longest)

        return _max

driver = Solution()
print(driver.longestConsecutive([100,4,200,1,3,2]))