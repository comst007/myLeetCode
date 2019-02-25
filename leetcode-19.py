# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        pcur = head
        ppre = None
        pnext = None
        if not head.next:
            if n == 1:
                return None
            else:
                return head

        pnext = pcur
        step = 1

        while step < n:
            pnext = pnext.next
            step = step + 1

        while pnext.next:
            ppre = pcur
            pcur = pcur.next
            pnext = pnext.next
        if not ppre:
            return head.next
        ppre.next = pcur.next

        return head


