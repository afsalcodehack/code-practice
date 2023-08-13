class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        return self.helper(root.left, root.right)

    def helper(self, n1, n2):

        if (n1 is None and n2 is not None) or (n2 is None and n1 is not None):
            return False;

        if n1 is None or n2 is None:
            return

        if n1.val != n2.val:
            return False

        result = self.helper(n1.left, n2.right)
        if result == False:
            return False
        result = self.helper(n1.right, n2.left)
        if result == False:
            return False
        return True


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)

t.left.left = TreeNode(3)
t.left.right = TreeNode(4)

t.right.left = TreeNode(4)
t.right.right = TreeNode(3)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(2)

t2.left.left = None
t2.left.right = TreeNode(3)

t2.right.left = None
t2.right.right = TreeNode(3)


t3 = TreeNode(1)


t4 = TreeNode(1)
t4.left = None
t4.right = TreeNode(2)


service = Solution()
print(service.isSymmetric(t)) #true

print(service.isSymmetric(t2)) #false

print(service.isSymmetric(t3)) #true

print(service.isSymmetric(t4)) #false
