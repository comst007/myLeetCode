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
    def swapPairs(self, head: ListNode):
        if not head:
            return None
        if not head.next:
            return head
        pcur = head
        while pcur and pcur.next:
            tmp = pcur.val
            pcur.val = pcur.next.val
            pcur.next.val = tmp

            pcur = pcur.next
            pcur = pcur.next
        return head

l1 = create_list([1,2,3,4])
sl = Solution()

res = sl.swapPairs(l1)

show(res)