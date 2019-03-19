class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, root: TreeNode, res_arr: list, k: int):

        if root.left:
            res = self.dfs(root.left, res_arr, k)
            if res is not None:
                return res

        res_arr.append(root.val)
        if len(res_arr) == k:
            return root.val

        if root.right:
            res = self.dfs(root.right, res_arr, k)
            if res is not None:
                return res

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        res = self.dfs(root, [], k)

        return res
