import math
from logging import root
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = self.dfs(root, -math.inf ,math.inf)
        print(res)

    def dfs(self, root, left , right):

        if root is None:
            return True

        if root.val <= left or root.val >= right:
            return False

        return self.dfs(root.left, left, root.val) and self.dfs(root.right, root.val, right)






head2 = TreeNode(5)
head2.left = TreeNode(3)
head2.left.left = TreeNode(2)
head2.left.right = TreeNode(4)

head2.right = TreeNode(8)
head2.right.left = TreeNode(6)
head2.right.right = TreeNode(9)

head = TreeNode(2)
head.left = TreeNode(1)
head.right = TreeNode(3)



driver = Solution()
driver.isValidBST(head2)
driver.isValidBST(head)
