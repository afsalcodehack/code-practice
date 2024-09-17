from typing import List


class Solution:

    def replaceElements2(self, arr: List[int]) -> List[int]:

        max = -1
        i = len(arr)-1
        while i >= 0:
            temp = arr[i]
            arr[i] = max
            if temp > max:
                max = temp
            i = i -1
        print(arr)


    def replaceElements(self, arr: List[int]) -> List[int]:

        max = 0
        max_pos = 0
        _len = len(arr)
        if _len <=0: return arr
        for i in range(0, _len):
            if max_pos == i:
                max = 0
                for j in range(i+1, _len):
                    if arr[j] > max:
                        max = arr[j]
                        max_pos = j

            arr[i] = max
        arr[_len-1] = -1

        print(arr)

driver = Solution()
driver.replaceElements([17,18,5,4,6,1])
driver.replaceElements([400])
driver.replaceElements([])
print('---------------------------------------')
driver.replaceElements2([17,18,5,4,6,1])
driver.replaceElements2([400])
driver.replaceElements2([])