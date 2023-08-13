from queue import Queue
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        marker = TreeNode('m')
        res = []
        temp = []
        q = Queue()
        q.put(root)
        q.put(marker)
        while not q.empty():

            n = q.get()

            if n == marker:
                res.append(temp)
                temp = []
                q.put(marker)
            else:
                if n is not None:
                    temp.append(n.val)
                    if n.left is not None:
                        q.put(n.left)
                    if n.right is not None:
                        q.put(n.right)
        return res[::-1]

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)

t.left.left = TreeNode(3)
t.left.right = TreeNode(4)

t.right.left = TreeNode(4)
t.right.right = TreeNode(3)


t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)

t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)

service = Solution()
print(service.levelOrderBottom(t))
print(service.levelOrderBottom(t1))