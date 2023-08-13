class Solution:
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if s[i:j+1] == (s[i:j+1])[::-1]:
                        if len(res) < (j+1) - i:
                            res = s[i:j+1]

        return res


call = Solution()
print(call.longestPalindrome("babad"))
print(call.longestPalindrome("a"))
print(call.longestPalindrome("aaaa"))