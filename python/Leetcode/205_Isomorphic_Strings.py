
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        _map1 = {}
        _map2 = set()

        for i, v in enumerate(s):

            if v in _map1:
                if _map1[v] != t[i]:
                    return False
            else:
                if t[i] in _map2:
                    return False
                else:
                    _map1[v] = t[i]
                    _map2.add(t[i])

        return True


driver = Solution()
print(driver.isIsomorphic("egg", "add"), True)
print(driver.isIsomorphic("foo", "bar"), False)
print(driver.isIsomorphic("paper", "title"), True)
print(driver.isIsomorphic("bbbaaaba", "aaabbbba"), False)
print(driver.isIsomorphic("badc", "baba"), False)
