from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        map = {}
        res = [-1] * len(nums1)

        for i,v in enumerate(nums2):
            map[v] = i;

        for i,v in enumerate(nums1):
            idx = map.get(v)

            for j in range(idx , len(nums2)):
                if v < nums2[j]:
                    res[i] = nums2[j]
                    break
        return res


    def nextGreaterElementWithMonotonicStack(self, nums1: List[int], nums2: List[int]) -> List[int]:

        map = {}
        res = [-1] * len(nums1)
        st = []
        for i, v in enumerate(nums1):
            map[v] = i

        for i, v in enumerate(nums2):
            while st:
                if st[-1] < v:
                    stv = st.pop()
                    idx = map.get(stv)
                    if idx is not None:
                        res[idx] = v
                else:
                    break
            st.append(v)
        return res


driver = Solution()
print(driver.nextGreaterElement([4,1,2], [1,3,4,2]))
print(driver.nextGreaterElement([4], [1,3,4,2]))
print(driver.nextGreaterElement([3], [1,3,4,2]))
print(driver.nextGreaterElement([2], [1,3,4,2]))

print('-----------------------------------')
print(driver.nextGreaterElementWithMonotonicStack([4,1,2], [1,3,4,2]))
print(driver.nextGreaterElementWithMonotonicStack([4], [1,3,4,2]))
print(driver.nextGreaterElementWithMonotonicStack([3], [1,3,4,2]))
print(driver.nextGreaterElementWithMonotonicStack([2], [1,3,4,2]))

