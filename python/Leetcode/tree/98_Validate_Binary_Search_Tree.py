from logging import root
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        if root.left is not None and root.left.val >= root.val:
            return False

        if root.right is not None and root.right.val <= root.val:
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)



head = TreeNode(2)
head.left = TreeNode(1)
head.right = TreeNode(3)

head2 = TreeNode(5)
head2.left = TreeNode(1)
head2.right = TreeNode(4)
head2.right.left = TreeNode(3)
head2.right.right = TreeNode(6)



driver = Solution()
print(driver.isValidBST(head))
print(driver.isValidBST(head2))
