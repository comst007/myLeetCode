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
    def _merge_sortlist(self, l1, l2):
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

    def mergeKLists(self, lists):
        cnt = len(lists)
        if cnt == 0:
            return None
        if cnt == 1:
            return lists[0]
        if cnt == 2:
            return self._merge_sortlist(lists[0], lists[1])
        mid = cnt // 2
        left_half = lists[:mid + 1]
        right_half = lists[mid+1:]
        res1 = self.mergeKLists(left_half)
        res2 = self.mergeKLists(right_half)
        res = self._merge_sortlist(res1, res2)
        return res

l1 = create_list([1,4,5])
l2 = create_list([1,3,4])
l3 = create_list([2,6])
arr = [l1,l2,l3]
sl = Solution()

res = sl.mergeKLists(arr)

show(res)
