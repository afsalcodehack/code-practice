from typing import List

#Bucket sorting
#https://www.youtube.com/watch?v=YPTqKIgVk-k
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        result = [[] for i in range(len(nums) + 1)]
        for i in nums:
            map[i] = 1 + map.get(i, 0)

        for n, c in map.items():
            result[c].append(n)
        final_result = []
        for i in range(len(result)-1, 0, -1):
            for j in result[i]:
                final_result.append(j)
                if len(final_result) == k:
                    return final_result




driver = Solution()
print(driver.topKFrequent([1,1,1,2,2,3], 2))
print(driver.topKFrequent([1,2,3,4,5,6,6], 3))
