class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        cnt_nd = 1
        node_arr = [root]
        cnt = 1
        while cnt:
            tmp_cnt = cnt
            cnt = 0
            tmp_node = []
            for i in range(tmp_cnt):
                if node_arr[i].left:
                    tmp_node.append(node_arr[i].left)
                    cnt += 1
                    cnt_nd += 1
                if node_arr[i].right:
                    tmp_node.append(node_arr[i].right)
                    cnt += 1
                    cnt_nd += 1
            node_arr = tmp_node
        return cnt_nd

