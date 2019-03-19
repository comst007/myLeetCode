class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root:TreeNode, sum:int, cur_sum:int):
        if not root.left and not root.right:
            if cur_sum + root.val == sum:
                return True
            else:
                return False
        if root.left:
            if self.dfs(root.left, sum, cur_sum + root.val):
                return True

        if root.right:
            if self.dfs(root.right, sum, cur_sum + root.val):
                return True

        return False

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        res = self.dfs(root, sum, 0)
        return  res 
