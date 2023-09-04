
class Solution:
    def subArraySum(self,arr, n, s): 
        sum = 0
        start = 0 
        end = 0
        for i in arr:
            sum = sum +  i
            if sum == s: break
            if sum > s:
                sum =sum - arr[start]
                start = start + 1
                if sum == s: break
            else:
                end = end +  1
        return[start+1 , end+1]


service = Solution()
print(service.subArraySum([1,2,3,7,5],4, 12))
print(service.subArraySum([1,2,3,4,5,6,7,8,9,10],10, 15))
print(service.subArraySum([1,2,3,4,5,6,7,8,9,10],10, 15))
print(service.subArraySum([135, 101, 170, 125, 79, 159, 163, 65, 106, 146 
                           ,82 ,28,162 ,92, 196, 143, 28 ,37, 192, 5 ,103, 154,
                             93, 183 ,22, 117, 119, 96, 48, 127, 172, 139 ,70, 
                             113, 68, 100, 36, 95, 104, 12, 123, 134],42, 468))
