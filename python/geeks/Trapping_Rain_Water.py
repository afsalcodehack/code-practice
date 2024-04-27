
class Solution:
    def trappingWater(self, arr,n):

        l = 0
        r = 1
        _sum = 0
        max_sum = -1
        max_index = 1
        blocks_count = 0
        zero_count = 0
        result = 0
        while r < len(arr):
            if arr[r] > 0:
                _sum = (min(arr[l], arr[r]) * (r-l-1)) - blocks_count
                print(_sum, arr[l], arr[r], blocks_count)
                if _sum <= max_sum and arr[l] < arr[r]:
                    l = max_index
                    r = l+1
                    result += max_sum
                else:
                    max_sum = _sum
                    max_index = r

            blocks_count += arr[r]

            r += 1
        return max(max_sum,result)


driver =Solution()
# print(driver.trappingWater([3,0,0,2,0,4], 6), 10)
# print(driver.trappingWater([7,4,0,9], 4), 10)
# print(driver.trappingWater([6,9,9], 3), 0)
# print(driver.trappingWater([8, 8, 2, 4, 5 ,5, 1], 7) , 3)
print(driver.trappingWater([1 ,1, 5, 2, 7, 6 ,1 ,4, 2, 3], 10) , 7)