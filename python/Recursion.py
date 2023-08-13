def palin(nums, data, start, k, size):

    if k > size:
        return

    print(data)

    while start < size:
        palin(nums, nums[start:k+1], start, k + 1, size)
        start += 1


a = ""
val = "1234"
palin(val, a, 0, 0, 4)

#print(val[0:1])
