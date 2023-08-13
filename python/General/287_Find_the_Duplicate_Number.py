class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        _len = len(nums)
        for i in range(0, _len):
            if i > 0:
                if nums[i] == nums[i-1]:
                    return nums[i]

service = Solution()
print(service.findDuplicate([1,3,4,2,2]))
print(service.findDuplicate([3,1,3,4,2]))
