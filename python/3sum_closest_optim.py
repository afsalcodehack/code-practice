import time
import test as data


class Solution:

    def threeSum(self, nums, target):
        length = len(nums)
        nums.sort()
        result = None

        print(nums)
        for i in range(0, length - 2):
 
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = int((length + i) / 2)
            right = length - 1

            while right > left > i:
                sum = nums[i] + nums[left] + nums[right]

                if sum == target:
                    return target

                if result is None:
                    result = sum

                if abs(sum - target) <= abs(result - target):
                    result = sum

                if sum < target:
                    left += 1
                else:
                    right -= 1
        return result


start_time = time.process_time()
service = Solution()
print(service.threeSum([-1, 2, 1, -4], 1)) #2
# print(service.threeSum([0,1,2], 0))
# print(service.threeSum([1,1,1,1], 0))
print(service.threeSum([0,2,1,-3], 1)) #0
print(service.threeSum([-1, 0, 1, 1, 55], 3))  # 2
# print(service.threeSum([1,1,-1,-1,3], -1) , -1)  #
# print("--- %s seconds ---" % (time.process_time() - start_time))
