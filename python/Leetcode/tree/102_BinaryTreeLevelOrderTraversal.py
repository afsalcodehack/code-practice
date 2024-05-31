# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.helper(root, 0, res)
        return res

    def helper(self, root, level, res):
        if root is None:
            return

        if len(res) <= level:
            res.append([])

        res[level].append(root.val)

        self.helper(root.left, level + 1, res)
        self.helper(root.right, level + 1, res)


head = TreeNode(3)
head.left = TreeNode(9)
head.right = TreeNode(20)

head.right.left = TreeNode(15)
head.right.right = TreeNode(7)

driver = Solution()
print(driver.levelOrder(head))
