class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        map_arr = [0] * 26
        res = 0

        for r in range(len(s)):

            map_arr[ord(s[r]) - ord('A')] += 1

            max_char_occ = 0

            for i in map_arr:
                max_char_occ = max(max_char_occ, i)
            if ((r - l + 1) - max_char_occ) <= k:
                res = max(res, (r - l + 1))
            else:
                if map_arr[ord(s[l]) - ord('A')] > 0:
                    map_arr[ord(s[l]) - ord('A')] -= 1
                l += 1
        return res


driver = Solution()
print(driver.characterReplacement('ABAB', 2))
print(driver.characterReplacement('AAAAA', 2))
print(driver.characterReplacement('ABCDD', 1))
print(driver.characterReplacement("IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR", 2)) #6
