class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1 or n == 2 or n == 0:
            return 1

        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        return res

service = Solution()
print(service.climbStairs(2))

