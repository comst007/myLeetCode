# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildRootWithPreAndin(self, preorder:list, l_pre:int, h_pre:int, inorder:list, l_in:int, h_in:int ):

        n_pre = h_pre - l_pre + 1
        n_in = h_in - l_in + 1
        if not n_pre and not n_in:
            return None
        if n_pre == 1 and n_in == 1:
            return TreeNode(preorder[l_pre])
        if n_pre != n_in:
            return None

        if h_pre < l_pre:
            return None

        root = TreeNode(preorder[l_pre])
        in_pos = inorder.index(preorder[l_pre], l_in, h_in + 1)
        n_left = in_pos - l_in

        root.left = self.buildRootWithPreAndin(preorder, l_pre + 1, l_pre + n_left, inorder, l_in, in_pos - 1)
        root.right = self.buildRootWithPreAndin(preorder, l_pre + n_left + 1, h_pre, inorder, in_pos + 1, h_in)
        return root
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        n_pre = len(preorder)
        n_in = len(inorder)
        if not n_pre and not n_in:
            return None
        if n_pre == 1 and n_in == 1:
            return TreeNode(preorder[0])
        if n_pre != n_in:
            return None
        root = TreeNode(preorder[0])
        pos_in = inorder.index(preorder[0])

        root.left = self.buildRootWithPreAndin(preorder, 1, pos_in , inorder, 0, pos_in - 1)
        root.right = self.buildRootWithPreAndin(preorder, pos_in + 1, n_pre - 1, inorder, pos_in + 1, n_in - 1)

        return root



