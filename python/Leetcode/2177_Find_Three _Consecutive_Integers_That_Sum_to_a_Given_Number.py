from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if (num - 3) % 3 != 0: return []
        startNumber = int((num - 3) / 3)
        return [startNumber, startNumber + 1, startNumber + 2]


driver = Solution()
print(driver.sumOfThree(33))
print(driver.sumOfThree(4))
print(driver.sumOfThree(4))
