class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def create_list(arr):
    if len(arr) == 0:
        return None
    head = None
    tail = None
    for x in arr:
        new_node = ListNode(x)
        if not head:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = tail.next

    return head


def show(head):
    pcur = head
    while pcur:
        print(pcur.val, ' ', end='')
        pcur = pcur.next
    print(" ")


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        ppre = head
        pnext = head.next
        while pnext:
            if pnext.val >= ppre.val:
                ppre = pnext
                pnext = pnext.next
            else:
                break

        if not pnext:
            return head

        pleft_head = None
        pleft_tail = None
        pright_head = None
        pright_tail = None

        pivot_node = head
        pcur = head.next
        while pcur:
            if pcur.val < pivot_node.val:
                if not pleft_head:
                    pleft_head = pcur
                    pleft_tail = pcur
                else:
                    pleft_tail.next = pcur
                    pleft_tail = pleft_tail.next
                pcur = pcur.next
                pleft_tail.next = None

            else:
                if not pright_head:
                    pright_head = pcur
                    pright_tail = pcur
                else:
                    pright_tail.next = pcur
                    pright_tail = pright_tail.next

                pcur = pcur.next
                pright_tail.next = None




        sorted_left = self.sortList(pleft_head)
        sorted_right = self.sortList(pright_head)

        res_head = None
        if not sorted_left:
            res_head = pivot_node

        else:
            res_head = sorted_left
            pcur = sorted_left
            while pcur.next:
                pcur = pcur.next
            pcur.next = pivot_node

        pivot_node.next  = sorted_right

        return res_head

l1 = create_list([4,2,1,3])
show(l1)

l2 = create_list([-1,5,3,4,0])
show(l2)

sl = Solution()
res1 = sl.sortList(l1)
show(res1)
res2 = sl.sortList(l2)
show(res2)
