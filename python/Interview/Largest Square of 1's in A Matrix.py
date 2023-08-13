import copy

def largestSquare(matrix):
    result = 0;
    cache = copy.deepcopy(arr)
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            cache[i][j] = min(cache[i-1][j], cache[i][j-1], cache[i-1][j-1]) + cache[i][j];
            if cache[i][j] > result:
                result = cache[i][j];
    return result;




arr = [[1, 1, 0, 1, 0],
           [0, 1, 1, 1, 0],
           [1, 1, 1, 1, 0],
           [0, 1, 1, 1, 1]
           ];
print(largestSquare(arr))



