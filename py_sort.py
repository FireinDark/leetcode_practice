# -*- coding: utf-8 -*-
__author__ = 'yi.liu'


# 冒泡排序
def bubble_sort(arr):
    # 用来提前终止排序
    status = True
    while status:
        status = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                status = True
    return arr


# 选择排序
# 另一种是用新列表来接收有序值，删除原数组中的值
def select_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# 插入排序
# 分为直接插入排序和折半插入排序，
# 折半插入即根据已存在的有序数组存放新值
# 增量为1， 步长为数组长度的希尔排序，
def insert_sort(arr):
    for i in range(len(arr)):
        pre_index = i - 1
        # 使用零食变量将当前值取出来，与之前的有序数组进行比较，进行插入
        # 相当于将该位置空出
        current = arr[i]
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index+1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index+1] = current
    return arr


# 希尔排序
# 称递减增量排序算法，是插入排序的一种更高效的改进版本
# 希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，
# 待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
# 一般将增量取为数组长度的一半
# 程序选用Knuth在1969年提出的步长序列：1 4 13 40 121 364 1093 3280 。。。后一个元素是前一个元素*3+1
def shell_sort(arr):
    step = 1
    while (step < len(arr) / 3):
        step = step * 3 + 1
    while step > 0:
        for i in range(step, len(arr)):
            tmp = arr[i]
            pre_index = i - step
            while pre_index >= 0 and arr[pre_index] > tmp:
                arr[pre_index+step] = arr[pre_index]
                pre_index -= step
            # 因为pre_index所在位置，总是比tmp应呆位置靠前一个
            arr[pre_index+step] = tmp
        step //= 3
    return arr




if __name__ == '__main__':
    d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]
    # print("冒泡排序结果： %s" % (bubble_sort(d0) == d0_out))
    # print("选择排序结果： %s" % (select_sort(d0) == d0_out))
    # print("插入排序结果： %s" % (insert_sort(d0) == d0_out))
    print("希尔排序结果： %s" % shell_sort(d0))

