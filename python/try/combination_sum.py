class Solution:


    def combinationSum(self, candidates, target: int):
        result = []
        self.combination_sum(candidates , 0, [],0 , target,result)
        return result

    def combination_sum(self , nums , pos, res,_sum , target,result):

        if pos >= len(nums):
            return

        if _sum > target:
            return

        if _sum == target:
            result.append(res[:])
            return

        res.append(nums[pos])
        _sum = _sum + nums[pos]
        self.combination_sum(nums,pos,res,_sum,target,result)
        res.pop()
        _sum = _sum - nums[pos]
        self.combination_sum(nums,pos+1,res,_sum,target,result)



driver = Solution()
print(driver.combinationSum([2,3,6,7], 7))
print(driver.combinationSum([2,3,5], 8))