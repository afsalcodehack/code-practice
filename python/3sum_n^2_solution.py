import time
import test as data


class Solution:
    result = []

    def threeSum(self, nums):
        length = len(nums)
        self.result.clear()
        nums.sort()
        for i in range(0, length - 2):

            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = length - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    self.result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1

                    left += 1
                    right -= 1
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
        return self.result


start_time = time.process_time()
val = [-1, 0, 1, 2, -1, -4]
service = Solution()
#print(service.threeSum(val))
#print(service.threeSum([0, 0, 0, 0]))
#
# print(service.threeSum([0, -1, 2, -3, 1]))
#
# print(service.threeSum([1, -2, 1, 0, 5]))
#
print(service.threeSum(
    [-2, -7, -11, -8, 9, -7, -8, -15, 10, 4, 3, 9, 8, 11, 1, 12, -6, -14, -2, -1, -7, -13, -11, -15, 11, -2, 7, -4, 12,
     7, -3, -5, 7, -7, 3, 2, 1, 10, 2, -12, -1, 12, 12, -8, 9, -9, 11, 10, 14, -6, -6, -8, -3, -2, 14, -15, 3, -2, -4,
     1, -9, 8, 11, 5, -14, -1, 14, -6, -14, 2, -2, -8, -9, -13, 0, 7, -7, -4, 2, -8, -2, 11, -9, 2, -13, -10, 2, 5, 4,
     13, 13, 2, -1, 10, 14, -8, -14, 14, 2, 10]))

# _dataService = data.three_sum_data()
# print(service.threeSum(_dataService.data))

# print(service.threeSum([-2,0,1,1,2]))

print("--- %s seconds ---" % (time.process_time() - start_time))
