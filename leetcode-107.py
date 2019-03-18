class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> list:

        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        res = []
        arr_val = [root.val]
        cur_nodes = [root]
        cnt = 1
        while cnt:
            res.append(arr_val[:])
            tmp_nodes = []
            tmp_val = []
            tmp_cnt = cnt
            cnt = 0
            for i in range(tmp_cnt):
                if cur_nodes[i].left:
                    tmp_nodes.append(cur_nodes[i].left)
                    tmp_val.append(cur_nodes[i].left.val)
                    cnt += 1

                if cur_nodes[i].right:
                    tmp_nodes.append(cur_nodes[i].right)
                    tmp_val.append(cur_nodes[i].right.val)
                    cnt += 1

            cur_nodes = tmp_nodes
            arr_val = tmp_val

        return res
    def levelOrderBottom(self, root: TreeNode) -> list:

        res = self.levelOrder(root)
        return list(reversed(res))

