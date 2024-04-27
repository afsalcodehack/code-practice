# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.helper(root)

        self.display(root)

    def display(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return

        print(root.val)

        if root.left is not None:
            self.display(root.left)

        if root.right is not None:
            self.display(root.right)

    def helper(self, root):

        temp = root.left
        root.left = root.right
        root.right = temp

        if root.left is not None:
            self.helper(root.left)

        if root.right is not None:
            self.helper(root.right)


head = TreeNode(4)
head.left = TreeNode(2)
head.right = TreeNode(7)

head.left.left = TreeNode(1)
head.left.right = TreeNode(3)

head.right.left = TreeNode(6)
head.right.right = TreeNode(9)

driver = Solution()
driver.invertTree(head)
