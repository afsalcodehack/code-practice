from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        map = {}
        max_val=nums[0],
        max_count = 1
        for i in nums:
            val = map.get(i , 0)
            if val != 0:
                val += 1
                map[i] = val
                if max_count < val:
                    max_val = i
                    max_count = val
            else:
                map[i] = 1
        return max_val

driver =Solution()
print(driver.majorityElement([3,2,3]))
print(driver.majorityElement([2,2,1,1,1,2,2]))
print(driver.majorityElement([1]))