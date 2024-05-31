# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = None
        curr = root
        for i in range(0,len(preorder)):

            if i is None:
                continue

            if root is None:
                root = TreeNode(i)
                curr = root
            else:
                if preorder[i] is not None:
                    curr.right = TreeNode(preorder[i])
                    curr = curr.right
                    inorder[i] = None

            idx = inorder.index(preorder[i])
            if idx:
                inorder[idx] = None
                curr.left = TreeNode(inorder[idx-1])

                if inorder[idx] in preorder:
                    preIdx = preorder.index(inorder[idx])
                    preorder[preIdx] = None
        return root

driver = Solution()
root = driver.buildTree([3,9,20,15,7],[3,9,20,15,7])
print(root.val)