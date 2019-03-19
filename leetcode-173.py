class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.st = []
        self.cnt = 0
        tmp = root
        while tmp:
            self.st.append(tmp)
            self.cnt += 1
            tmp = tmp.left



    def next(self) -> int:
        """
        @return the next smallest number
        """
        top = self.st.pop()
        self.cnt -= 1
        if top.right:
            tmp = top.right
            while tmp:
                self.st.append(tmp)
                self.cnt += 1
                tmp = tmp.left
        return top.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.cnt:
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()