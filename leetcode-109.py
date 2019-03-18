class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        ppre = None
        pfast = head
        plast = head
        while pfast:
            pfast = pfast.next
            if pfast:
                pfast = pfast.next
            else:
                break
            ppre = plast
            plast = plast.next


        proot = plast
        pleft = None
        if not ppre:
            pleft = None
        else:
            pleft = head
            ppre.next = None

        pright = plast.next
        plast.next = None

        root = TreeNode(proot.val)
        root.left = self.sortedListToBST(pleft)
        root.right = self.sortedListToBST(pright)
        return root
