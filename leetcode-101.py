# Definition for a binary tree node.
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
    def isHW(self, arr:list):
        n = len(arr)
        if not n:
            return True
        if n == 1:
            return True
        l = 0
        h = n - 1
        while l < h:
            if arr[l] is None and arr[h] is None:
                l += 1
                h -= 1
            elif not arr[l] and arr[h]:
                return False
            elif arr[l] and not arr[h]:
                return False
            else:

                if arr[l] != arr[h]:
                    return False
                else:
                    l += 1
                    h -= 1

        return True
    def isSymmetric(self, root: TreeNode) -> bool:

        if not root:
            return True
        if root.left and not root.right:
            return False
        if not root.left and root.right:
            return False
        arr_node = [root]
        arr_tmp = []
        arr_val = [root.val]
        null_val = None
        cnt = 1
        while cnt:
            arr_val = []
            tmp_cnt = cnt
            cnt = 0
            for i in range(tmp_cnt):
                if arr_node[i].left:
                    cnt += 1
                    arr_tmp.append(arr_node[i].left)
                    arr_val.append(arr_node[i].left.val)
                else:
                    arr_val.append(null_val)

                if arr_node[i].right:
                    cnt += 1
                    arr_tmp.append(arr_node[i].right)
                    arr_val.append(arr_node[i].right.val)
                else:
                    arr_val.append(null_val)
            if not self.isHW(arr_val):
                return False
            arr_node = arr_tmp
            arr_tmp = []

        return True

sl = Solution()

tree = treeFromArrWithLevelTraverse([1,2,2,3,4,4,3])

res = sl.isSymmetric(tree)
print(res)