class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def traverse_pre(self, root:TreeNode, nodes:list):



        if root.left:
            if not self.traverse_pre(root.left, nodes):
                return False


        if len(nodes) > 0 and root.val <= nodes[-1]:
            return False
        else:
            nodes.append(root.val)

        if root.right:
            if not self.traverse_pre(root.right, nodes):
                return False

        return True


    def isValidBST(self, root:TreeNode) -> bool:
        if not root:
            return True

        res = self.traverse_pre(root, [])
        return res