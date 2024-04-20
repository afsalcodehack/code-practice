from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        _len = len(nums)
        i = 0
        while i < (_len - 2):

            l = i + 1
            r = _len - 1

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            while l < r and r > l:
                _sum = nums[i] + nums[l] + nums[r]
                if _sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                elif _sum > 0:
                    r -= 1
                else:
                    l += 1
            i += 1
        return result




driver = Solution()
print(driver.threeSum([-2,0,0,2,2]))
print(driver.threeSum([-1,0,1,2,-1,-4]))
print(driver.threeSum([0,1,1]))
print(driver.threeSum([0,0,0]))
print(driver.threeSum([]))