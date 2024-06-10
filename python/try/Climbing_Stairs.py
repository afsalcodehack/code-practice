class Solution:
    def __init__(self):
        self._map = {}

    def climbStairs(self, n: int) -> int:
       return self.climb(n,0)

    def climb(self,n, i):

        if i >= n:
            return 1

        if (i + 2) in self._map:
            return self._map[i + 2]

        res = self.climb(n, i+1)

        if (n-i) >= 2:
            res += self.climb(n, i+2)

        return res

driver = Solution()
print(driver.climbStairs(38))

