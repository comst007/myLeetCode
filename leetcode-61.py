# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
    def rotateRight(self, head:ListNode, k: int) -> ListNode:
        if not head:
            return head
        if not head.next:
            return head
        if k == 0:
            return head
        pfast = head
        pslow = head
        ppreslow = None
        cnt = 0
        while pfast and cnt < k:
            pfast = pfast.next
            cnt += 1
        if not pfast:
            k = k % cnt
            if k == 0:
                return head
            cnt = 0
            pfast = head
            while pfast and cnt < k:
                pfast = pfast.next
                cnt += 1

        while pfast.next:
            pfast = pfast.next
            pslow = pslow.next

        phead_new = pslow.next
        pslow.next = None
        pfast.next = head

        return phead_new


sl = Solution()

l1 = create_list([1,2,3,4,5])

res = sl.rotateRight(l1, 2)

show(res)

sl = Solution()

l2 = create_list([0,1,2])
res = sl.rotateRight(l2, 4)
show(res)