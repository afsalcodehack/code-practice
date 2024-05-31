# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if p is None or q is None:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.right.left = TreeNode(4)

head2 = TreeNode(1)
head2.left = TreeNode(2)
head2.right = TreeNode(3)
head2.right.left = TreeNode(4)

driver = Solution()
print(driver.isSameTree(head, head2))