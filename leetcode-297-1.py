class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ""
        if not root:
            return ""
        st = [root]
        cnt = 1
        while cnt:
            cur = st.pop()
            cnt -= 1
            if cur is None:
                res += '__#__'
                continue
            else:
                res += '__{}__'.format(cur.val)
            st.append(cur.right)
            cnt += 1
            cur = cur.left
            while cur:
                res += '__{}__'.format(cur.val)
                st.append(cur.right)
                cnt += 1
                cur = cur.left

            st.append(None)
            cnt += 1
        return res

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

    def rootWithPreorder(self, nodes:list):
        n = len(nodes)
        if not n:
            self.root = None
        root = TreeNode(nodes[0])
        right, lchild = self.makeTree(nodes, n, 1)

        _, rchild = self.makeTree(nodes, n, right)

        root.left = lchild
        root.right = rchild
        return root
    def rootWithPreorder_norecurse(self, nodes:list):
        st = []
        visit_dict = {}
        n = len(nodes)
        root = TreeNode(nodes[0])
        visit_dict[root] = 0
        st.append(root)
        i = 1
        while i < n:
            top = st[-1]
            if nodes[i] is None:
                if visit_dict[top] == 0:
                    visit_dict[top] = 1
                elif visit_dict[top] == 1:
                    st.pop()
            else:
                new_nd = TreeNode(nodes[i])
                if visit_dict[top] == 0:
                    visit_dict[top] = 1
                    top.left = new_nd
                    visit_dict[new_nd] = 0
                    st.append(new_nd)
                elif visit_dict[top] == 1:
                    top.right = new_nd
                    visit_dict[new_nd] = 0
                    st.pop()
                    st.append(new_nd)
            i += 1

        return root
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        n = len(data)
        if not n:
            return None
        nodes_arr = []
        i = 0
        j = 0
        while i < n:
            cnt_ = 0
            j = i
            while cnt_ < 4:
                if data[j] == '_':
                    cnt_ += 1
                j += 1
            cur_val = data[i:j].strip('_')
            if cur_val == '#':
                nodes_arr.append(None)
            else:
                nodes_arr.append(int(cur_val))
            i = j

        root = self.rootWithPreorder_norecurse(nodes_arr)
        return root

# sl = Codec()
#
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
#
# n1.left = n2
# n1.right = n3
# n3.left = n4
# n3.right = n5
#
# root = n1
#
# res = sl.serialize(root)
#
# new_root = sl.deserialize(res)
#
# print("dd")

# sl = Codec()
#
# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n4 = TreeNode(4)
# n5 = TreeNode(5)
#
# n1.right = n2
# n2.right = n3
# n3.right = n4
# n4.right = n5
#
# root = n1
#
# res = sl.serialize(root)
#
# new_root = sl.deserialize(res)
#
# print("dd")


sl = Codec()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n2.left = n3
n2.right = n4
n4.left = n5
root = n1

res = sl.serialize(root)

new_root = sl.deserialize(res)

print("dd")

