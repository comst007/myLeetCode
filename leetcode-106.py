class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def builRootWithinAndPos(self, inorder:list, postorder:list):

        n_in = len(inorder)
        n_post = len(postorder)
        if n_in != n_post:
            return None
        if not n_in and not n_post:
            return None
        if n_in == 1 and n_post == 1:
            return TreeNode(postorder[-1])

        root = TreeNode(postorder[-1])

        in_pos = inorder.index(postorder[-1])

        root.left = self.builRootWithinAndPos(inorder[:in_pos], postorder[:in_pos])
        root.right = self.builRootWithinAndPos(inorder[in_pos + 1:], postorder[in_pos:n_post - 1])
        return root
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        n_in = len(inorder)
        n_post = len(postorder)
        if n_in != n_post:
            return None
        if not n_in and not n_post:
            return None
        if n_in == 1 and n_post == 1:
            return TreeNode(postorder[-1])

        root = TreeNode(postorder[-1])

        in_pos = inorder.index(postorder[-1])

        root.left = self.builRootWithinAndPos(inorder[:in_pos], postorder[:in_pos])
        root.right = self.builRootWithinAndPos(inorder[in_pos + 1:], postorder[in_pos:n_post - 1])

        return root



