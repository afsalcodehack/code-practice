import time


class Solution:
    result = []

    def threeSum(self, nums):
        temp = []
        length = len(nums)
        self.result.clear()
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                for k in range(j + 1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp.extend([nums[i], nums[j], nums[k]])
                        temp.sort()
                        if temp not in self.result:
                            self.result.append(temp[:])
                    temp.clear()
        return self.result


start_time = time.process_time()
val = [-1, 0, 1, 2, -1, -4]
service = Solution()
print(service.threeSum(val))
print(service.threeSum([0]))
# print(service.threeSum(
#     [-2, -7, -11, -8, 9, -7, -8, -15, 10, 4, 3, 9, 8, 11, 1, 12, -6, -14, -2, -1, -7, -13, -11, -15, 11, -2, 7, -4, 12,
#      7, -3, -5, 7, -7, 3, 2, 1, 10, 2, -12, -1, 12, 12, -8, 9, -9, 11, 10, 14, -6, -6, -8, -3, -2, 14, -15, 3, -2, -4,
#      1, -9, 8, 11, 5, -14, -1, 14, -6, -14, 2, -2, -8, -9, -13, 0, 7, -7, -4, 2, -8, -2, 11, -9, 2, -13, -10, 2, 5, 4,
#      13, 13, 2, -1, 10, 14, -8, -14, 14, 2, 10]))
print("--- %s seconds ---" % (time.process_time() - start_time))
