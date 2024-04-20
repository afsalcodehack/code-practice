import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []
        result_pos = 0
        map = {}
        for i in range(len(strs)):
            l_map = {}
            for j in range(len(strs[i])):
                l_map[strs[i][j]] = 1 + l_map.get(strs[i][j], 0)
            str_sorted = ''.join(sorted(strs[i]))
            if str_sorted in map:
                result[map[str_sorted]].append(strs[i])
            else:
                map[str_sorted] = result_pos
                result.append([strs[i]])
                result_pos += 1
        return result


class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            print(tuple(count))
            ans[tuple(count)].append(s)
        return ans.values()


driver = Solution2()
print(driver.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(driver.groupAnagrams(["a"]))
print(driver.groupAnagrams([""]))
