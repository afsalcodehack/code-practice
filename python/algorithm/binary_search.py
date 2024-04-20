import math


def binarySearch(nums , key):

    mid = math.floor(len(nums) / 2)
    start = 0
    count = 0
    while start < mid:
        count += 1
        if nums[start] == key:
            return mid, count
        if nums[mid] == key:
            return mid, count
        if nums[mid] < key:
            start = mid
            mid = math.floor((len(nums) + mid) / 2)
            print('mid left' , mid)
        else:
            mid = math.floor((start + mid) / 2)
            print('mid right', mid)
    return -1, count


print(binarySearch([1,2,3,4,5,6,7] , 7))
print(binarySearch([1,2,3,4,5,6,7] , 6))
print(binarySearch([1,2,3,4,5,6,7] , 5))
print(binarySearch([1,2,3,4,5,6,7] , 4))
print(binarySearch([1,2,3,4,5,6,7] , 3))
print(binarySearch([1,2,3,4,5,6,7] , 2))
print(binarySearch([1,2,3,4,5,6,7] , 1))
print(binarySearch([1,2,3,4,5,6,7] , 12))
print(binarySearch([1,2,3,4,5,6,7] , 0))