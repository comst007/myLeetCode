class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treeRootinLevel(nodes:list, k:int):
    n = len(nodes)
    if k >= n:
        return None
    if nodes[k] is None:
        return None
    root = TreeNode(nodes[k])
    root.left = treeRootinLevel(nodes, 2 * k + 1)
    root.right = treeRootinLevel(nodes, 2 * k + 2)
    return root

def treeFromArrWithLevelTraverse(nodes:list):
    root = TreeNode(nodes[0])
    left = treeRootinLevel(nodes, 1)
    right = treeRootinLevel(nodes,2)
    root.left = left
    root.right = right
    return root

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        level = 1
        nodes_arr = [root]
        cnt = 1
        while True:
            tmp_cnt = cnt
            cnt = 0
            nodes_tmp = []
            for i in range(tmp_cnt):
                if not nodes_arr[i].left and not nodes_arr[i].right:
                    return level
                if nodes_arr[i].left:
                    nodes_tmp.append(nodes_arr[i].left)
                    cnt += 1
                if nodes_arr[i].right:
                    nodes_tmp.append(nodes_arr[i].right)
                    cnt += 1

            level += 1
            nodes_arr = nodes_tmp

root = treeFromArrWithLevelTraverse([1,2,3,4,5])
sl = Solution()

res = sl.minDepth(root)