# -*- coding: utf-8 -*-
__author__ = 'yi.liu'

"""
暴力算法，速度慢
exits_list = list(range(len(lists)))
result = list()
record = dict()
while exits_list:
    min_val = None
    null_Node = False
    for i in exits_list:
        if record.get(i) is None:
            if not lists[i]:
                exits_list.remove(i)
                null_Node = True
                break
            else:
                record[i] = lists[i]
        if min_val is None:
            min_val = record[i].val
            min_index = i
        else:
            if record[i].val < min_val:
                min_val = record[i].val
                min_index = i
    if not null_Node:
        result.append(min_val)
        if record[min_index].next:
            record[min_index] = record[min_index].next
        else:
            exits_list.remove(min_index)
return result

"""


# 方法2
# def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#     # 先将链表两两合并，最后返回一个列表
#     if not lists:
#         return []
#     if len(lists) == 1:
#         return lists
#     if len(lists) == 2:
#         return self.merge_two_list(*lists)
#     return self.mergeKLists([self.merge_two_list(lists[0], lists[1]), lists[2:]])
#
# def merge_two_list(self, a, b):
#     new = ListNode(0)
#     current = new
#     while a and b:
#         if a.val < b.val:
#             current.next = a
#             a = a.next
#         else:
#             current.next = b
#             b = b.next
#         current = current.next
#     if a:
#         current.next = a
#     if b:
#         current.next = b
#     return new.next

# 方法3
"""
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    # 先将链表两两合并，最后返回一个列表
    if not lists:
        return []
    from functools import reduce
    return reduce(self.merge_two_list, lists)

def merge_two_list(self, a, b):
    new = ListNode(0)
    current = new
    while a and b:
        if a.val < b.val:
            current.next = a
            a = a.next
        else:
            current.next = b
            b = b.next
        current = current.next
    if a:
        current.next = a
    if b:
        current.next = b
    return new.next
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        n = len(lists)
        return self.merge(lists, 0, n - 1)

    def merge(self, lists, left, right):
        # print("传入参数", lists, left, right)
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        # print("L1", l1)
        l2 = self.merge(lists, mid + 1, right)
        # print("l2", l2)

        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    a = [[1], [2], [3], [4], [5]]
    print("最终结果", Solution().merge(a, 0, 4))



