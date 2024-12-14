from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        if len(text) < len('balloon'):
            return 0

        total = len(text)
        _map = Counter('balloon')
        _count = Counter(text)
        for key in 'balloon':
            total = min(total,  _count[key] / _map[key])

        if total < 0:
            return 0
        else:
            return int(total)


driver = Solution()
print(driver.maxNumberOfBalloons("nlaebolko"))
print(driver.maxNumberOfBalloons("loonbalxballpoon"))
print(driver.maxNumberOfBalloons("leetcode"))
print(driver.maxNumberOfBalloons("lloo"))  #0
print(driver.maxNumberOfBalloons("ballook"))  #0
print(driver.maxNumberOfBalloons("balloon"))  #0


