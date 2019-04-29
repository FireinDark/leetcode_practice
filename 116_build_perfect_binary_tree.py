# -*- coding: utf-8 -*-
__author__ = 'yi.liu'

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        # 此题和117类似
        # 如果父结点同时有左右节点， 那么左节点直接指向其右节点就行
        # 如果只有左节点，那么就看父节点的next指向的右侧节点是否存在 左右节点，优先返回左节点
        if root.left and root.right:
            root.left.next = root.right
        elif root.left:
            root.left.next = self.find_next(root.next)
        if root.right:
            root.right.next = self.find_next(root.next)
        # 优先遍历右侧节点，因为左侧节点都要使用对右侧节点的引用
        # 若不优先遍历，则root.next基本为空
        self.connect(root.right)
        self.connect(root.left)
        return root

    def find_next(self, root):
        if not root:
            return None
        if root.left:
            return root.left
        elif root.right:
            return root.right
        return None