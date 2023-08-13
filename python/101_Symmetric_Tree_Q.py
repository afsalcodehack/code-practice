from queue import Queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        q1 = Queue()
        q2 = Queue()

        q1.put(root.left)
        q2.put(root.right);
        return self.helper(q1, q2)

    def helper(self, q1, q2):

        l1 = []
        l2 = []

        while True:
            n1 = q1.get()
            n2 = q2.get()

            if (n1 is None and n2 is not None) or (n1 is not None and n2 is None):
                return False

            if n1 is None and n2 is None:
                return True

            l1.append(n1.val)
            l2.append(n2.val)

            if l1 != l2:
                return False

            q1.put(n1.left)
            q2.put(n2.right)
            q1.put(n1.right)
            q2.put(n2.left)

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

t2.left.left = TreeNode(None)
t2.left.right = TreeNode(3)

t2.right.left = TreeNode(None)
t2.right.right = TreeNode(3)

t3 = TreeNode(1)

t4 = TreeNode(1)
t4.left = TreeNode(None)
t4.right = TreeNode(2)

service = Solution()
print(service.isSymmetric(t))  # true

print(service.isSymmetric(t2))  # false

print(service.isSymmetric(t3))  # true

print(service.isSymmetric(t4))  # false
