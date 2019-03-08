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
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head

        left_head = None
        left_tail = None
        right_head = None
        right_tail = None

        pcur = head
        while pcur:
            if pcur.val < x:
                if left_head is None:
                    left_head = pcur
                    left_tail = pcur
                else:
                    left_tail.next = pcur
                    left_tail = left_tail.next
            else:
                if right_head is None:
                    right_head = pcur
                    right_tail = pcur
                else:
                    right_tail.next = pcur
                    right_tail = right_tail.next

            pcur = pcur.next

        if left_tail:
            left_tail.next = right_head
            if right_tail:
                right_tail.next = None
            return left_head
        else:
            right_tail.next = None
            return right_head

l1 = create_list([1,4,3,2,5,2])
x = 3
sl = Solution()
show(l1)
res = sl.partition(l1,x)

show(res)