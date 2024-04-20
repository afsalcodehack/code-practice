# User function Template for python3
# https://www.geeksforgeeks.org/problems/two-repeated-elements-1587115621/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
class Solution:

    def twoRepeated(self, arr, n):
        res = []
        for i in range(len(arr)):
            if arr[abs(arr[i])] > 0:
                arr[abs(arr[i])] = -arr[abs(arr[i])]
            else:
                res.append(abs(arr[i]))
        return res

driver = Solution()
print(driver.twoRepeated([1,2,1,3,4,3], 4))
print(driver.twoRepeated([1,2,2,1], 2))

