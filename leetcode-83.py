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
    def deleteDuplicates(self, head: ListNode):
        if not head:
            return head
        pnew_head = head
        pnew_tail = head
        pcur = head.next
        while pcur:
            if pcur.val == pnew_tail.val:
                pcur = pcur.next
            else:
                pnew_tail.next = pcur
                pnew_tail = pnew_tail.next
                pcur = pcur.next

        pnew_tail.next = None

        return pnew_head



sl = Solution()
l1 = create_list([1,1,2])
res1 = sl.deleteDuplicates(l1)
show(res1)
l2 = create_list([1,1,2,3,3])
res2 = sl.deleteDuplicates(l2)

show(res2)


