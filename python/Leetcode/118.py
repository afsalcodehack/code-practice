from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = []
        for i in range(0, numRows):
            t = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    t.append(1)
                else:
                    t.append(res[i - 1][j] + res[i - 1][j - 1])
            res.append(t)
        return res


driver = Solution()
print(driver.generate(2))
