from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        _len = len(nums)
        ans = [0] * (_len * 2)
        for i in  range(_len):
            ans[i] = nums[i]
            ans[_len + i] = nums[i]
        print(ans)

driver = Solution()
driver.getConcatenation([1,2,1])
driver.getConcatenation([1,3,2,1])

