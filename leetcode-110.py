class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def depth(self, root:TreeNode):
        if not root:
            return 0, True
        left_depth, isbalanced1 = self.depth(root.left)
        right_depth, isbalanced2 = self.depth(root.right)

        return max(left_depth, right_depth) + 1, abs(left_depth - right_depth) <= 1 and isbalanced1 and isbalanced2

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return True
        dep, isbalanced = self.depth(root)
        return isbalanced


sl = Solution()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.right = n3


res = sl.isBalanced(n1)