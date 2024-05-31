from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = root.val

        # return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = max(dfs(root.left), 0)
            rightMax = max(dfs(root.right), 0)

            # compute max path sum WITH split
            self.res = max(res, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return self.res



head = TreeNode(5)
head.left = TreeNode(3)
head.right = TreeNode(6)
head.left.right = TreeNode(4)

head.left.left = TreeNode(2)
head.left.left.left = TreeNode(1)

driver = Solution()
print(driver.maxPathSum(head))