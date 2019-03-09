# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MyTree:
    def __init__(self, val = 0):
        root = TreeNode(val)
        self.root = root
    def makeTree(self, nodes:list, n:int, pos:int):
        if pos >= n:
            return pos, None

        if nodes[pos] is None:
            return pos + 1, None

        root_cur = TreeNode(nodes[pos])

        next, lchild = self.makeTree(nodes, n, pos + 1)


        next, rchild = self.makeTree(nodes,n, next)

        root_cur.left = lchild
        root_cur.right = rchild

        return next, root_cur

    def __init__(self, nodes:list):
        n = len(nodes)
        if not n:
            self.root = None
        self.root = TreeNode(nodes[0])
        right, lchild = self.makeTree(nodes, n, 1)

        _, rchild = self.makeTree(nodes, n, right)

        self.root.left = lchild
        self.root.right = rchild


class Solution:
    def traverse_in(self, root:TreeNode, res:list):
        if root.left:
            self.traverse_in(root.left, res)
        res.append(root.val)
        if root.right:
            self.traverse_in(root.right, res)

    def traverse_in_norecurse(self, root:TreeNode, res:list):

        pcur = root
        st = []
        while True:
            while pcur:
                st.append(pcur)
                pcur = pcur.left
            if not len(st):
                break

            pcur = st.pop()
            res.append(pcur.val)
            pcur = pcur.right




        return res

    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        res = []
        self.traverse_in_norecurse(root, res)
        return res


t = MyTree([1,None,2,3])

sl = Solution()

res = sl.inorderTraversal(t.root)
print(res)