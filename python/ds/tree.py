# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_sum = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)

    def helper(self, root, count):
        if root is None:
            self.max_sum = max(self.max_sum, count)
            return self.max_sum

        self.helper(root.left, count + 1)
        self.helper(root.right, count + 1)

        return self.max_sum


head = TreeNode(4)
head.left = TreeNode(2)
head.right = TreeNode(7)

head.left.left = TreeNode(1)
head.left.right = TreeNode(3)

head.right.left = TreeNode(6)
head.right.right = TreeNode(9)

head.right.right.right = TreeNode(10)
head.right.right.right.right = TreeNode(11)

driver = Solution()

print('max dept' , driver.maxDepth(head))
