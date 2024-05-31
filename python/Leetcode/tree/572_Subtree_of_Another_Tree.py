# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSameTree(root.left, subRoot) or self.isSameTree(root.right, subRoot)

    def isSameTree(self, p, q) -> bool:

        if not p and not q:
            return True

        if  p or  q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

class Solution2:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False


head = TreeNode(3)
head.left = TreeNode(4)
head.right = TreeNode(5)
head.left.left = TreeNode(1)
head.left.right = TreeNode(2)

# head2 = TreeNode(4)
# head2.left = TreeNode(1)
# head2.right = TreeNode(2)

head2 = TreeNode(2)

driver = Solution2()
print(driver.isSubtree(head, head2))
