class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MyTree:
    def __init__(self, val=0):
        root = TreeNode(val)
        self.root = root

    def __init__(self, nodes: list):
        n = len(nodes)
        if not n:
            self.root = None
        self.root = TreeNode(nodes[0])
        right, lchild = self.makeTree(nodes, n, 1)

        _, rchild = self.makeTree(nodes, n, right)

        self.root.left = lchild
        self.root.right = rchild

    def makeTree(self, nodes: list, n: int, pos: int):
        if pos >= n:
            return pos, None

        if nodes[pos] is None:
            return pos + 1, None

        root_cur = TreeNode(nodes[pos])

        next, lchild = self.makeTree(nodes, n, pos + 1)

        next, rchild = self.makeTree(nodes, n, next)

        root_cur.left = lchild
        root_cur.right = rchild

        return next, root_cur


class Solution:
    def makeTree(self, nodes: list, n: int, pos: int):
        if pos >= n:
            return pos, None

        if nodes[pos] is None:
            return pos + 1, None

        root_cur = TreeNode(nodes[pos])

        next, lchild = self.makeTree(nodes, n, pos + 1)

        next, rchild = self.makeTree(nodes, n, next)

        root_cur.left = lchild
        root_cur.right = rchild

        return next, root_cur
    def treeFromlist(self, nodes:list):
        n = len(nodes)
        root = None
        if not n:
            root = None
        root = TreeNode(nodes[0])
        right, lchild = self.makeTree(nodes, n, 1)

        _, rchild = self.makeTree(nodes, n, right)

        root.left = lchild
        root.right = rchild
        return root

    def generateTree_between(self, start:int, end:int,visit:dict):
        if (start, end) in visit:
            return visit[(start, end)][:]
        if start > end:
            visit[(start, end)] = [[None]]
            return [[None]]
        if start == end:
            visit[(start, end)] = [[start, None, None]]
            return [[start, None, None]]

        sub_res = []
        left_res = []
        right_res = []
        res = []

        for i in range(start, end + 1):
            sub_res = []
            left_res = []
            right_res = []

            left_res = self.generateTree_between(start, i - 1, visit)

            right_res = self.generateTree_between(i + 1, end,visit)

            for x in left_res:
                for y in right_res:
                    res.append([i] + x[:] + y[:])


        visit[(start, end)] = res[:]

        return res

    def generateTrees(self, n: int):
        res = []
        visit = {}
        res = self.generateTree_between(1,n,visit)

        res = [ self.treeFromlist(x) for x in res]
        return res




sl = Solution()

res = sl.generateTrees(3)

for x in res:
    print(x)

