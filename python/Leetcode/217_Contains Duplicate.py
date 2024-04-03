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


    def containsDuplicateWithSet(self, nums: List[int]) -> bool:
        _map = set()
        for i in nums:
            if i in _map:
                return True
            else:
                _map.add(i)
        return False



driver = Solution()
print(driver.containsDuplicateWithSet([1,2,3,1]))
print(driver.containsDuplicateWithSet([1,2,3,4]))
print(driver.containsDuplicateWithSet([1,1,1,3,3,4,3,2,4,2]))
print(driver.containsDuplicateWithSet([1]))
