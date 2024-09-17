from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        _map = {}

        for i in range(len(s)):

            if s[i] in _map:

                if t[i] != _map[s[i]]:
                    return False
            else:
                if t[i] in _map and _map[t[i]] == s[i]:
                    return False
                _map[s[i]] = t[i]

        return True


driver = Solution()
print(driver.isIsomorphic("egg", "add") , True)
print(driver.isIsomorphic("foo", "bar"), False)
print(driver.isIsomorphic("paper", "title"), True)
print(driver.isIsomorphic("bbbaaaba", "aaabbbba"), False)
print(driver.isIsomorphic("badc", "baba"), False)