import time
class Solution:
    result = []

    def threeSum(self, nums):
        self.result.clear()

        def comb(self, arr, k, p, temp):
            if k == len(temp):
                if (sum(temp)) == 0:
                    n = temp[:]
                    n.sort()
                    if n not in self.result:
                        self.result.append(n[:])
                return

            for i in range(p, len(arr)):
                temp.append(arr[i])
                comb(self, arr, k, i + 1, temp)
                del temp[-1]

        t = [] * 3
        comb(self, nums, 3, 0, t)
        return self.result

start_time = time.process_time()
val = [-1, 0, 1, 2, -1, -4]
service = Solution()
#print(service.threeSum(val))
print(service.threeSum([-2,-7,-11,-8,9,-7,-8,-15,10,4,3,9,8,11,1,12,-6,-14,-2,-1,-7,-13,-11,-15,11,-2,7,-4,12,7,-3,-5,7,-7,3,2,1,10,2,-12,-1,12,12,-8,9,-9,11,10,14,-6,-6,-8,-3,-2,14,-15,3,-2,-4,1,-9,8,11,5,-14,-1,14,-6,-14,2,-2,-8,-9,-13,0,7,-7,-4,2,-8,-2,11,-9,2,-13,-10,2,5,4,13,13,2,-1,10,14,-8,-14,14,2,10]))
print("--- %s seconds ---" % (time.process_time() - start_time))