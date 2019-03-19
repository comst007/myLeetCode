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
        node_arr = [root]
        cnt = 1
        while cnt:
            tmp_cnt = cnt
            cnt = 0
            tmp_arr = []
            for i in range(len(node_arr)):
                if node_arr[i] is None:
                    tmp_arr.append(None)
                    tmp_arr.append(None)
                    res = res + '__#__'
                    continue
                else:
                    res = res + '__{}__'.format(node_arr[i].val)

                    if node_arr[i].left:
                        tmp_arr.append(node_arr[i].left)
                        cnt += 1
                    else:
                        tmp_arr.append(None)

                    if node_arr[i].right:
                        tmp_arr.append(node_arr[i].right)
                        cnt += 1
                    else:
                        tmp_arr.append(None)
            node_arr = tmp_arr
        return res

    def treeRootinLevel(self, nodes: list, k: int):
        n = len(nodes)
        if k >= n:
            return None
        if nodes[k] is None:
            return None
        root = TreeNode(nodes[k])
        root.left = self.treeRootinLevel(nodes, 2 * k + 1)
        root.right = self.treeRootinLevel(nodes, 2 * k + 2)
        return root

    def treeFromArrWithLevelTraverse(self, nodes: list):
        root = TreeNode(nodes[0])
        left = self.treeRootinLevel(nodes, 1)
        right = self.treeRootinLevel(nodes, 2)
        root.left = left
        root.right = right
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

        root = self.treeFromArrWithLevelTraverse(nodes_arr)
        return root

sl = Codec()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

root = n1

res = sl.serialize(root)

new_root = sl.deserialize(res)
