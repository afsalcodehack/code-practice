from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if len(digits) <= 0: return []
        i = len(digits) - 1

        while True:
            if digits[i] + 1 <= 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
                    break
                else:
                    i -= 1

        return digits


service = Solution()
# print(service.plusOne([1,2,3]))
# print(service.plusOne([4,3,2,1]))
# print(service.plusOne([9,9,9]))
# print(service.plusOne([1]))
print(service.plusOne([8,9,9,9]))