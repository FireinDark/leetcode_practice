

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    f = head
    for _ in range(n):
        f = f.next
    
    cur = head
    while f:
        f = f.next
        cur = cur.next
    cur.next = cur.next.next
    return head
    

        
    


if __name__ == '__main__':
    main()
    