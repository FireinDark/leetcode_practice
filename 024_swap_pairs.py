
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    temp = ListNode(0, head)
    cur = temp
    while cur.next and cur.next.next:
        a = cur.next
        b = cur.next.next
        c = cur.next.next.next
        cur.next = b
        b.next = a
        a.next = c
        cur = cur.next.next
    return temp.next


def swapPairs2(head):
    if not head or not head.next:
        return None
    new_head = head.next
    head.next = swapPairs2(new_head.next)
    new_head.next = head
    return new_head