# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root.val == p.val or root.val == q.val:
            return root

        if p.val < root.val < q.val or p.val > root.val > q.val:
            return root

        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)


head = TreeNode(6)
head.left = TreeNode(2)
head.right = TreeNode(8)

head.left.left = TreeNode(0)
head.left.right = TreeNode(4)

head.left.right.left = TreeNode(3)
head.left.right.right = TreeNode(5)

head.right.left = TreeNode(7)
head.right.right = TreeNode(9)

head2 = TreeNode(2)

driver = Solution()
print(driver.lowestCommonAncestor(head, head.left, head.right).val)
print(driver.lowestCommonAncestor(head, head.right.left, head.right.right).val)
