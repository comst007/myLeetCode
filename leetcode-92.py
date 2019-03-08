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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pcur = None
        pstart = None
        pend = None
        ppre = None
        pend_next = None
        if not head:
            return head
        if not head.next:
            return head
        if m == n:
            return head
        k = 1
        pcur = head
        while k < m:
            ppre = pcur
            pcur = pcur.next
            k += 1

        pstart = pcur
        while k < n:
            pcur = pcur.next
            k += 1
        pend = pcur

        pend_next = pend.next

        phead_new = None
        phead_tail = None
        if ppre is None:
            phead_new = None
            phead_tail = pstart
            pcur = pstart
            while pcur != pend:
                ptmp = pcur.next
                pcur.next = phead_new
                phead_new = pcur
                pcur = ptmp
            pcur.next = phead_new
            phead_new = pcur
            phead_tail.next = pend_next
            return phead_new

        else:
            phead_new = head
            ppre.next = None
            pcur = pstart
            phead_tail = pstart
            while pcur != pend:
                tmp = pcur.next
                pcur.next = ppre.next
                ppre.next = pcur
                pcur = tmp
            pcur.next = ppre.next
            ppre.next = pcur
            phead_tail.next = pend_next
            return phead_new

        pass

# sl = Solution()
#
# l1 = create_list([1,2,3,4,5])
# show(l1)
# res = sl.reverseBetween(l1,2,4)
# show(res)

sl = Solution()

l1 = create_list([3,5])
show(l1)
res = sl.reverseBetween(l1,1,2)
show(res)