class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root:TreeNode, res:list):

        res.append(root.val)
        if root.left:
            self.dfs(root.left, res)
        if root.right:
            self.dfs(root.right, res)

    def preorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        res = []
        self.dfs(root, res)
        return res

