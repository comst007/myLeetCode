class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelTraverse(self, root:TreeNode, res:list):

        node_arr = [root]
        cnt = 1
        while cnt:
            tmp_cnt = cnt
            tmp_node = []
            res.append(node_arr[-1].val)

            cnt = 0
            for i in range(tmp_cnt):
                if node_arr[i].left:
                    tmp_node.append(node_arr[i].left)
                    cnt += 1
                if node_arr[i].right:
                    tmp_node.append(node_arr[i].right)
                    cnt += 1

            node_arr = tmp_node



    def rightSideView(self, root: TreeNode) -> list:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        res = []
        self.levelTraverse(root,res)
        return res