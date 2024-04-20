from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        _max_sum = 0
        while l < r and r > l:
            _sum = min(height[l], height[r]) * (r - l)
            _max_sum = max(_max_sum , _sum)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return _max_sum


driver = Solution()
print(driver.maxArea([1,8,6,2,5,4,8,3,7]))
print(driver.maxArea([2,3,4,5,18,17,6]))
print(driver.maxArea([1,1]))
print(driver.maxArea([]))
print(driver.maxArea([1]))