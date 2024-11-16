from typing import List


class NumArray:
    sumArr = []

    def __init__(self, nums: List[int]):
        _sum = 0
        self.sumArr = [0] * len(nums)
        for i, v in enumerate(nums):
            _sum += v
            self.sumArr[i] = _sum

    def sumRange(self, left: int, right: int) -> int:
        left_sum = 0 if left == 0 else self.sumArr[left-1]
        return self.sumArr[right] - left_sum


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2,0,3,-5,2,-1])
param_1 = obj.sumRange(0,2)
print(param_1)

obj = NumArray([-1])
param_2 = obj.sumRange(0,0)
print(param_2)
