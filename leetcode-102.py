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

sl = Solution()
tree = treeFromArrWithLevelTraverse([3,9,20, None, None, 15,7])
res = sl.levelOrder(tree)
for x in res:
    print(x)


