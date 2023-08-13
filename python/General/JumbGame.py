def jump(nums):
    count = 0
    size = len(nums)
    if size <= 1:
        return 0
    step = 0
    while step <= size:
        if (size - (step + 1)) <= nums[step]:
            return count + 1
        max_step_sum = 0
        for i in range(step + 1, (nums[step] + step+1)):
            _max = i + nums[i]
            if _max >= max_step_sum:
                max_step_sum = _max
                step = i
        count += 1

    return count


print(jump([2, 3, 1, 1, 4]))
print(jump([2, 1, 2, 3, 4, 2, 1, 3, 4]))
print(jump([2, 3, 1, 1, 6, 2, 1, 8]))
print(jump([1, 1, 1, 1, 2, 2, 2, 1]))
print(jump([0]))
