# 28. Find the Index of the First Occurrence in a String
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) <= 0 or len(needle) > len(haystack): return -1
        for i in range(0, len(haystack)):
            h_index = i
            needle_index = 0;
            while needle_index < len(needle) and h_index < len(haystack):
                if haystack[h_index] != needle[needle_index]:
                    break
                if needle_index == len(needle)-1:
                    return i
                needle_index = needle_index + 1
                h_index = h_index + 1
        return -1


service = Solution()

assert service.strStr("", "aaaa") == -1  # -1
print(service.strStr("aaa", "aaaa"))  # -1
print(service.strStr("sadbutsad", "but"))  # 3
print(service.strStr("affsasal", "sal"))  # 5
print(service.strStr("sadbutsad", "buta"))  # -1
print(service.strStr("sadbutsad", ""))  # -1
print(service.strStr("mississippi", "issip"))  # 4
print(service.strStr("mississipi", "issipi"))  # 4
