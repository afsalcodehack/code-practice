class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        if len(s) == 0: return 0
        i = len(s) - 1
        count = 0
        while s[i] != " " and i > -1:
            count += 1
            i -= 1
        return count


service = Solution()
print(service.lengthOfLastWord("a "))
