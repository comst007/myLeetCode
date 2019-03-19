
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,root:TreeNode, sum:int, cur_sum:int, sub_res:list, total_res:list):
        if not root.left and not root.right:
            if sum == cur_sum + root.val:
                sub_res.append(root.val)
                total_res.append(sub_res[:])
                sub_res.pop()
                return
            else:
                return

        sub_res.append(root.val)
        if root.left:
            self.dfs(root.left,sum, cur_sum + root.val, sub_res, total_res)

        if root.right:
            self.dfs(root.right, sum, cur_sum + root.val, sub_res, total_res)

        sub_res.pop()

    def pathSum(self, root: TreeNode, sum: int) -> list:
        if not root:
            return []
        res = []
        self.dfs(root,sum,0,[],res)
        return res
