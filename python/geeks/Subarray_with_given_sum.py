
class Solution:
    def subArraySum(self,arr, n, s): 
        sum = 0
        start = 0 
        end = 0
        while end < n :
            if sum == s: return [start+1, end]
            if sum < s:
                sum += arr[end]
                if sum > s:
                    sum -= arr[start]
                    start += 1
                else:
                    end += 1
            else:
                sum -= arr[start]
                start += 1
                if sum == s: return [start+1, end+1]
        if sum != s: return -1    
        return [start, end]

service = Solution()
print(service.subArraySum([1,2,3,7,5],5, 10000))  #-1
print(service.subArraySum([1,2,3,7,5],5, 15))     # [3,5]
print(service.subArraySum([1,2,3,4,5,6,7,8,9,10],10, 15)) #  [1,5]
print(service.subArraySum([1,2,3,4,5,6,7,8,9,10],10, 18)) #  [3,6]
print(service.subArraySum([ 135, 101, 170, 125, 79,   159, 163, 65, 106, 146 
                            ,82 , 28,  162 ,92,  196,  143, 28 , 37, 192, 5 ,
                            103, 154,  93, 183   ,22,  117, 119, 96, 48, 127,
                            172, 139 , 70, 113,  68,   100, 36,  95, 104, 12,
                            123, 134],42, 468)) #38 42

print(service.subArraySum([68, 100, 36,  95, 104, 12,
                            123, 134],8, 468)) #4 8
