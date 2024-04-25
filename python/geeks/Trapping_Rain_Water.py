
class Solution:
    def trappingWater(self, arr,n):

        l = 0
        r = 1
        _sum = 0
        max_sum = 0
        blocks_count = 0
        emptyspace = 0

        while r < len(arr):
            _sum = min(arr[l], arr[r]) * emptyspace
            print(_sum , arr[l], arr[r])
            if arr[r] >= arr[l]:
                 max_sum += _sum - blocks_count
                 _sum ,blocks_count, emptyspace = 0,0,0
                 l = r
                 r = l + 1
            else:
                emptyspace += 1
                blocks_count += arr[r]
            r += 1
        return max(max_sum, _sum)

driver =Solution()
# print(driver.trappingWater([3,0,0,2,0,4], 6), 10)
# print(driver.trappingWater([7,4,0,9], 4), 10)
# print(driver.trappingWater([6,9,9], 3), 0)
# print(driver.trappingWater([8, 8, 2, 4, 5 ,5, 1], 7) , 3)
print(driver.trappingWater([1 ,1, 5, 2, 7, 6 ,1 ,4, 2, 3], 10) , 7)