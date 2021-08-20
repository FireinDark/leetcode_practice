


from typing import List


def reverseList(head: ListNode) -> ListNode:
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev
    
        

        
        
        
    