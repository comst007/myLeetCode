class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        res = 0
        cur_nodes = [root]
        cnt = 1
        while cnt:
            res += 1
            tmp_nodes = []
            tmp_cnt = cnt
            cnt = 0
            for i in range(tmp_cnt):
                if cur_nodes[i].left:
                    tmp_nodes.append(cur_nodes[i].left)
                    cnt += 1

                if cur_nodes[i].right:
                    tmp_nodes.append(cur_nodes[i].right)
                    cnt += 1


            cur_nodes = tmp_nodes




        return res