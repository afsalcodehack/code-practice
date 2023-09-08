class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        A1 = sorted(A1)
        _map = {}
        res = []
        for i in A1:
            if i in _map:
                _map[i] = _map[i] + 1
            else:
                _map[i] = 1

        for i in A2:
            _count = _map.get(i, 0)
            for j in range(0, _count):
                res.append(i)
            _map.pop(i,None)
        
        for i in _map:
            res.append(i)
        return res
    

service = Solution()
print(service.relativeSort([2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8] , 11 ,[2, 1, 8, 3] , 4))