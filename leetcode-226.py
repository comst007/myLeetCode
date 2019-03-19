class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if not root.right and not root.left:
            return root
        left = root.left
        right = root.right

        if left:
            left = self.invertTree(left)
        if right:
            right = self.invertTree(right)
        root.left = right
        root.right = left
        return root



