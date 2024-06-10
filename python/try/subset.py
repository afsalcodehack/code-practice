
class Solution:

    def subset(self , nums , pos, res):

        if pos >= len(nums):
            return

        res.append(nums[pos])

        print(res)
        self.subset(nums, pos+1, res)

        res.pop()

        self.subset(nums, pos+1, res)

driver = Solution()
driver.subset([1,2,3],0, [])

