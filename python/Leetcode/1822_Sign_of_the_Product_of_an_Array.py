from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        _sum = 1;
        for i in nums:
            _sum = _sum * i;
        if _sum < 0: return -1
        if _sum == 0: return 0
        if _sum > 0: return 1


service = Solution()

print(service.arraySign([1, 5, 0, 2, -3]))
print(service.arraySign([-1, -2, -3, -4, 3, 2, 1]))
print(service.arraySign([-1, 1, -1, 1, -1]))
print(service.arraySign([]))