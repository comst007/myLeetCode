class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root:TreeNode, res_max:list):
        if not root.left and not root.right:
            if res_max[0] is None or res_max[0] < root.val:
                res_max[0] = root.val
            return root.val

        max_left = None
        max_right = None
        res = root.val
        if root.left:
            max_left = self.dfs(root.left, res_max)
            if max_left > 0:
                res += max_left
        if root.right:
            max_right = self.dfs(root.right, res_max)
            if max_right > 0:
                res += max_right

        if res_max[0] is None or res_max[0] < res:
            res_max[0] = res

        if max_left is None:
            if max_right > 0:
                return root.val + max_right
            else:
                return root.val
        elif max_right is None:
            if max_left > 0:
                return root.val + max_left
            else:
                return root.val
        else:
            biger = max(max_left, max_right)
            if biger > 0:
                return root.val + biger
            else:
                return root.val



    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        res_max = [None]
        self.dfs(root, res_max)

        return res_max[0]
