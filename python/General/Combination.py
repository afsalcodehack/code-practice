def print_combination(arr, n, r):
    data = [0] * r
    combination_util(arr, data, 0, n - 1, 0, r)


def combination_util(arr, data, start, end, index, r):
    if index == r:
        for j in range(r):
            print(data[j], end=" ")
        print()
        return

    i = start
    for j in range(i, end+1):
        data[index] = arr[j]
        combinationUtil(arr, data, j + 1,
                        end, index + 1, r)


arr = [1, 2, 3, 4, 5]
r = 3
n = len(arr)
print_combination(arr, n, r)
