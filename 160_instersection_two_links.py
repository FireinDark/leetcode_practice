# -*- coding: utf-8 -*-
__author__ = 'yi.liu'

# 方法1
"""
if headA == None or headB == None:
    return None

# 统计两链表长度
tagA = headA
len_A = 0
while tagA != None:
    len_A += 1
    tagA = tagA.next

tagB = headB
len_B = 0
while tagB != None:
    len_B += 1
    tagB = tagB.next

if len_A == len_B:
    # 两链表一起向前走，直到相交为止
    while headA != headB:
        headA = headA.next
        headB = headB.next
    return headA

for i in range(abs(len_B-len_A)):
    if len_B > len_A:
        headB = headB.next
    if len_A > len_B:
        headA = headA.next

# 两链表一起向前走，直到相交为止
while headA != headB:
    headA = headA.next
    headB = headB.next

return headA
"""


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None
        taga, tagb = headA, headB
        # 在这里第一轮体现在pA和pB第一次到达尾部会移向另一链表的表头, 而第二轮体现在如果pA或pB相交就返回交点, 不相交最后就是null==null
        while taga != tagb:
            taga = headB if taga is None else taga.next
            tagb = headA if tagb is None else tagb.next
        return taga