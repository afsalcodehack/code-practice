class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False
        map = {}
        for i in t:
            if i not in map:
                map[i] = 1
            else:
                map[i] += 1

        for i in s:
            if i not in map or map[i] == 0:
                return False
            else:
                map[i] -= 1
        return True


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False
        s_map = {}
        t_map = {}
        for i in range(len(t)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[s[i]] = 1 + t_map.get(s[i], 0)

        if s_map == t_map:
            return True
        else:
            return False


driver = Solution2()
print(driver.isAnagram('afsal', 'salaf'))
