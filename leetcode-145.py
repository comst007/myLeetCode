class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def treeRootinLevel(nodes:list, k:int):
    n = len(nodes)
    if k >= n:
        return None
    if nodes[k] is None:
        return None
    root = TreeNode(nodes[k])
    root.left = treeRootinLevel(nodes, 2 * k + 1)
    root.right = treeRootinLevel(nodes, 2 * k + 2)
    return root

def treeFromArrWithLevelTraverse(nodes:list):
    root = TreeNode(nodes[0])
    left = treeRootinLevel(nodes, 1)
    right = treeRootinLevel(nodes,2)
    root.left = left
    root.right = right
    return root

class Solution:
    def dfs(self, root: TreeNode, res: list):
        if root.left:
            self.dfs(root.left, res)
        if root.right:
            self.dfs(root.right, res)
        res.append(root.val)
    def dfs_norecurse(self, root:TreeNode):
        res = []
        st = []
        dict_visit = {}
        cnt = 0
        st.append(root)
        dict_visit[root] = 0
        cnt = 1
        while cnt:
            top = st[-1]
            if dict_visit[top] == 2:
                cnt -= 1
                res.append(top.val)
                st.pop()
            elif dict_visit[top] == 1:
                if top.right:
                    dict_visit[top] = 2
                    tmp_node = top.right
                    while tmp_node:
                        st.append(tmp_node)
                        dict_visit[tmp_node] = 1
                        cnt += 1
                        tmp_node = tmp_node.left



                else:
                    res.append(top.val)
                    cnt -= 1
                    st.pop()
            elif dict_visit[top] == 0:
                dict_visit[top] = 1
                tmp_node = top.left
                while tmp_node:
                    st.append(tmp_node)
                    dict_visit[tmp_node] = 1
                    cnt += 1
                    tmp_node = tmp_node.left

        return res




    def postorderTraversal(self, root: TreeNode) -> list:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        res = self.dfs_norecurse(root)
        return res

# t1 = treeFromArrWithLevelTraverse([1, None, 2,None, None, 3, None])
# sl = Solution()
#
# res = sl.postorderTraversal(t1)
#
# print(res)

t1 = treeFromArrWithLevelTraverse([1,2])
sl = Solution()

res = sl.postorderTraversal(t1)

print(res)