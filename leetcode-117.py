class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None
        if not root.left and not root.right:
            return root

        arr_nodes = [root]
        cnt = 1
        while cnt:
            tmp_cnt = cnt
            tmp_nodes = []
            cnt = 0

            for i in range(tmp_cnt):
                if arr_nodes[i].left:
                    tmp_nodes.append(arr_nodes[i].left)
                    cnt += 1
                if arr_nodes[i].right:
                    tmp_nodes.append(arr_nodes[i].right)
                    cnt += 1
                if i + 1 < tmp_cnt:
                    arr_nodes[i].next = arr_nodes[i + 1]

            arr_nodes = tmp_nodes


        return root