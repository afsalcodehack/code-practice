from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _map = {}
        for i in nums:
            if i in _map:
                return True
            else:
                _map[i] = 1
        return False



driver = Solution()
print(driver.containsDuplicate([1,2,3,1]))
print(driver.containsDuplicate([1,2,3,4]))
print(driver.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(driver.containsDuplicate([1]))
