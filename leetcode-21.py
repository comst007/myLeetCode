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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if not l1:
            return l2
        if not l2:
            return l1

        pnew_head = None
        pnew_tail = None

        p1 = l1
        p2 = l2
        if p1.val <= p2.val:
            pnew_head = p1
            pnew_tail = p1
            p1 = p1.next
        else:
            pnew_head = p2
            pnew_tail = p2
            p2 = p2.next

        while p1 and p2:
            if p1.val <= p2.val:
                pnew_tail.next = p1
                p1 = p1.next
                pnew_tail = pnew_tail.next
            else:
                pnew_tail.next = p2
                p2 = p2.next
                pnew_tail = pnew_tail.next

        if p1:
            pnew_tail.next = p1
        if p2:
            pnew_tail.next = p2

        return pnew_head



l1 = create_list([1,2,4])
l2 = create_list([1,3,4])

sl = Solution()
res = sl.mergeTwoLists(l1, l2)

show(res)