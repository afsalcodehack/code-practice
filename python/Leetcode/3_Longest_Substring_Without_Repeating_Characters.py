class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "" or s is None: return 0

        _max = 0
        l, r = 0, 1
        _map = {s[l]: True}
        while r < len(s):

            if s[r] in _map:
                _max = max(_max, r - l)
                l = _map[s[r]] + 1
                _map = {s[l]: l}
                r = l
            else:
                _map[s[r]] = r
            r += 1
        return max(_max, r - l + 1)

    def lengthOfLongestSubstring2(self, s: str) -> int:

        if s == "" or s is None: return 0

        _max = 0
        l = 0
        charSet = set()
        res = 0
        for r in range(len(s)):
            if s[r] in charSet:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l += 1
            charSet.add(s[r])

            res = max(res, r - l + 1)
        return res


driver = Solution()
print(driver.lengthOfLongestSubstring2("pwwkew"))  #3
print(driver.lengthOfLongestSubstring2("abcabcbb"))  #3
print(driver.lengthOfLongestSubstring2("abcdefg"))  #7
print(driver.lengthOfLongestSubstring2(""))  #0
print(driver.lengthOfLongestSubstring2("dvdf"))  #3
