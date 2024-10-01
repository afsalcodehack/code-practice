class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) <= 0: return False
        pos = 0
        for i in t:
            if s[pos] == i:
                pos += 1
            if pos == len(s):
                return True
        return False

driver = Solution()
print(driver.isSubsequence('abc', 'ahbgdc'))
print(driver.isSubsequence('axc', 'ahbgdc'))
print(driver.isSubsequence('bad', 'ahbgdc'))
print(driver.isSubsequence('', 'ahbgdc'))
print(driver.isSubsequence('', ''))