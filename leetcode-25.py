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
    def reverseKGroup(self, head: ListNode, k: int):
        if not head:
            return None
        if not head.next:
            return head
        pnew_head = None
        pnew_tail = None

        pcur_end = None
        pcur_start = head
        pcur = head
        step = 1
        while True:
            pcur = pcur_start
            step = 1
            while pcur and step < k:
                step = step + 1
                pcur = pcur.next


            if not pcur:
                if not pnew_head:
                    return head
                else:
                    pnew_tail.next = pcur_start
                    break

            pcur_end = pcur

            pcur = pcur_start

            ptmp_head = None
            ptmp_tail = pcur
            pnext = None
            while pcur != pcur_end:
                pnext = pcur.next
                pcur.next = ptmp_head
                ptmp_head = pcur
                pcur = pnext

            pcur_start = pcur_end.next

            pcur.next = ptmp_head
            ptmp_head = pcur
            if not pnew_head:
                pnew_head = ptmp_head
                pnew_tail = ptmp_tail
            else:
                pnew_tail.next = ptmp_head
                pnew_tail = ptmp_tail

            pnew_tail.next = None
            if not pcur_start:
                break




        return pnew_head



l1 = create_list([1,2,3,4,5])
l2 = create_list([1,2,3,4,5])

sl = Solution()

res1 = sl.reverseKGroup(l1, 2)
show(res1)

res2 = sl.reverseKGroup(l2, 3)
show(res2)
