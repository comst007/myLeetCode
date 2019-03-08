# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traverse_in(self, root:TreeNode, res:list):
        if root.left:
            self.traverse_in(root.left, res)
        res.append(root.val)
        if root.right:
            self.traverse_in(root.right, res)


    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        res = []
        self.traverse_in(root, res)
        return res
