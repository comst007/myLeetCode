# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode):
        if not head:
            return head
        pnew_head = None
        pnew_tail = None
        pcur = head
        cnt = 0
        while True:
            cnt = 1
            while pcur.next and pcur.val == pcur.next.val:
                cnt = cnt + 1
                pcur = pcur.next
            if pcur.next:
                if cnt == 1:
                    if pnew_head is None:
                        pnew_head = pcur
                        pnew_tail = pcur
                    else:
                        pnew_tail.next = pcur
                        pnew_tail = pnew_tail.next
                    pcur = pcur.next
                else:
                    pcur = pcur.next
            else:
                if cnt == 1:
                    if pnew_head is None:
                        pnew_head = pcur
                        pnew_tail = pcur
                    else:
                        pnew_tail.next = pcur
                        pnew_tail = pnew_tail.next
                    break
                else:
                    break

        if not pnew_head:
            return None
        else:
            pnew_tail.next = None
            return pnew_head



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


l1 = create_list([1,2,3,3,4,4,5])
show(l1)

l2 = create_list([1,1,1,2,3])
show(l2)

sl = Solution()

res1 = sl.deleteDuplicates(l1)
show(res1)

res2 = sl.deleteDuplicates(l2)
show(res2)



