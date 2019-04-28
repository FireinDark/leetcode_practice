# -*- coding: utf-8 -*-
__author__ = 'yi.liu'

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Node:
    def __init__(self, val, isLeaf, topLeft,
                 topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid) -> 'Node':
        # 将区间4等分表示4叉树
        # 比如8x8的分成 4个4x4的，
        # 如果区分后的区域值完全一样，那么他就是叶子节点
        is_leaf, val = self.is_leaf(grid)
        root = Node(val, is_leaf, None, None, None, None)
        if not is_leaf:
            half_index = int(len(grid) / 2)
            root.topLeft = self.construct(
                [row[0:half_index] for row in grid[0:half_index]])
            root.topRight = self.construct(
                [row[half_index:] for row in grid[0:half_index]])
            root.bottomLeft = self.construct(
                [row[0:half_index] for row in grid[half_index:]])
            root.bottomRight = self.construct(
                [row[half_index:] for row in grid[half_index:]])
        return root

    def is_leaf(self, grid) -> tuple:
        start = grid[0][0]
        is_leaf = True
        length = len(grid)
        for i in range(length):
            for j in range(length):
                if grid[i][j] != start:
                    is_leaf = False
                    val = True
                    break
        if is_leaf:
            val = True if start else False
        return is_leaf, val


if __name__ == '__main__':
    l = [[0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0]]
    n = Solution().construct(l)
