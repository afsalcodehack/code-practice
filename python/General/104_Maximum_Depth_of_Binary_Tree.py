class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    _max = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.helper(root, 0)
        print(self._max)

    def helper(self, root, _length):

        if root is None:
            if _length > self._max:
                self._max = _length
            return

        self.helper(root.left, _length + 1)
        self.helper(root.right, _length + 1)


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)

t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.left.right.right = TreeNode(4)
t.left.right.right.left = TreeNode(4)

t.right.left = TreeNode(4)
t.right.right = TreeNode(3)

service = Solution()
service.maxDepth(t)
