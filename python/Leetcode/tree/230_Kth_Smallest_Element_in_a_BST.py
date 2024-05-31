# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        return self.helper(root, k, 0)

    def helper(self,root, k , count):
        if root is None:
            return

        self.helper(root.left, k, count)
        print(count, root.val)
        self.helper(root.right, k, count + 1)





head = TreeNode(5)
head.left = TreeNode(3)
head.right = TreeNode(6)
head.left.right = TreeNode(4)

head.left.left = TreeNode(2)
head.left.left.left = TreeNode(1)

driver = Solution()
print(driver.kthSmallest(head, 3))
