from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], t: int) -> bool:
        count = 0
        if t == 0: return True
        for i, n in enumerate(flowerbed):
            if ((i - 1) < 0 or flowerbed[i - 1] == 0) and ((i + 1) > len(flowerbed) - 1 or flowerbed[i + 1] == 0) and n != 1:
                flowerbed[i] = 1
                count += 1
                if count >= t:
                    return True
        return False


driver = Solution()
print(driver.canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(driver.canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(driver.canPlaceFlowers([1, 0, 0, 0, 1], 4))
