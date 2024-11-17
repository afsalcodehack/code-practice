from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i,v in enumerate(nums):
            nums[v - 1] = 0
        print(nums)
        for i in nums:
            if i != 0:
                res.append(i+1)

        return res;



driver =Solution()
print(driver.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
