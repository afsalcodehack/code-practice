from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                return [map[nums[i]], i]
            else:
                map[(target-nums[i])] = i


driver = Solution()
print(driver.twoSum([2,7,11,15] , 9))
print(driver.twoSum([3,2,4] , 6))
print(driver.twoSum([3,3] , 6))
