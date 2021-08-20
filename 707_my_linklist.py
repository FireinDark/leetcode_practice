
# 单链表
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



class MyLinkedList:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.size = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if 0 <= index < self.size:
            node = self.head
            for _ in range(index+1):
                node = node.next
            return node.val
        return -1


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        
        self.size += 1
        
        new = Node(val)
        prev = self.head
        for _ in range(index):
            prev = prev.next
        new.next = prev.next
        prev.next = new


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > self.size:
            return
        self.size -= 1
        prev = self.head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        
        
def p(l):
    cur = l.head
    while cur:
        print(cur.val)
        cur = cur.next
        
    
    
if __name__ == '__main__':
    m = MyLinkedList()
    print(m.addAtHead(1))
    print(m.addAtTail(3))
    print(m.addAtIndex(1, 2))
    # p(m)
    # print(m.get(0))
    print(m.get(1))
    print(m.deleteAtIndex(1))
    print(m.get(1))
    
    
        
# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1]]