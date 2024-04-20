from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        map =  {}
        print(nums)
        _len = len(nums)
        i = 0
        j = 1

        while i < (_len - 3):
            j = i + 1
            while j < (_len - 2):
                k = j + 1
                while k < _len:
                    if (nums[i] + nums[j] + nums[k]) > 0:
                        break
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        result.append([nums[i], nums[j], nums[k]])
                        print(result)
                    k += 1
                j += 1
            i += 1
        return result


driver = Solution()
driver.threeSum([-1,0,1,2,-1,-4])