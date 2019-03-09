class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traverse_pre(self, p:TreeNode, q:TreeNode):
        if not p and q:
            return False
        if not p and not q:
            return True
        if p and not q:
            return False
        if p.val != q.val:
            return False
        if not self.traverse_pre(p.left,q.left):
            return False
        if not self.traverse_pre(p.right,q.right):
            return False
        return True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and q:
            return False
        if not p and not q:
            return True
        if p and not q:
            return False

        res = self.traverse_pre(p,q)
        return res


