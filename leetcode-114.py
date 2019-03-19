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
    def dfs(self, root:TreeNode, tail:TreeNode):
        if not root:
            return tail
        if not root.left and not root.right:
            tail.right = root
            return root

        pleft = root.left
        pright = root.right
        root.left = None
        root.right = None
        tail.right = root
        tail = root
        res = None
        if pleft:
            res = self.dfs(pleft, tail)
            tail = res
        if pright:
            res = self.dfs(pright, tail)

        return res
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        pleft = root.left
        pright = root.right
        root.left = None
        root.right = None
        ptail = root
        res = self.dfs(pleft, ptail)
        res = self.dfs(pright, res)

root = treeFromArrWithLevelTraverse([1,2,5,3,4,None,6])
sl = Solution()

sl.flatten(root)


