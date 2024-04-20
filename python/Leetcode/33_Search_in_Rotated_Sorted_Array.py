from typing import List

class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) -1

        while l < r:

            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # left
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        if nums[l] == target:
            return l

        return -1


driver = Solution()

print(driver.search([5,1,3], 3), 2)
print(driver.search([1,3], 3) , 1)
print(driver.search([5,1,3], 5) , 0)
print(driver.search([4,5,6,7,0,1,2], 0), 4)
print(driver.search([4,5,6,7,0,1,2], 1), 5)
print(driver.search([4,5,6,7,0,1,2], 4), 0)
print(driver.search([4,5,6,7,0,1,2], 6), 2)
print(driver.search([4,5,6,7,0,1,2], 2), 6)
print(driver.search([4,5,6,7,0,1,2], 5), 1)
print(driver.search([4,5,6,7,0,1,2], 15), -1)
