from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 0
        for i in range(0, len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) <= i:
                    return strs[0][0:count]
                if strs[j][i] != c:
                    return strs[0][0:count]
            count += 1
        return strs[0][0:count]


driver = Solution()
print(driver.longestCommonPrefix(["flower","flow","flight"]))
print(driver.longestCommonPrefix(["abc","abcd","ab"]))
print(driver.longestCommonPrefix(["abc"]))
print(driver.longestCommonPrefix([""]))