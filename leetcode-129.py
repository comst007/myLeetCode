class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root:TreeNode, sub_sum:int, total_sum:list):
        if not root.left and not root.right:
            total_sum[0] += sub_sum * 10 + root.val
        sub_sum = sub_sum * 10 + root.val
        if root.left:
            self.dfs(root.left,sub_sum,total_sum)
        if root.right:
            self.dfs(root.right, sub_sum,total_sum)

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        res = [0]
        self.dfs(root, 0, res)
        return res[0]
