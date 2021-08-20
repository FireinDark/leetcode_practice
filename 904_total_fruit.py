


def totalFruit(fruits):
    if len(fruits) <= 2:
        return len(fruits)
    # 第一个篮子 left 第二个篮子 right
    left = right = 0
    # 记录两个篮子 第一个出现的位置
    temp = 0
    # 最大长度 total
    total = 0
    for i in range(len(fruits)):
        # 表示出现了一个新的需要第三个篮子
        if fruits[i] != fruits[left] and fruits[i] != fruits[right]:
            if left != right:
                left = temp
            right = i
        total = max(total, i-left+1)
        if fruits[i] != fruits[temp]:
            temp = i
    return total


if __name__ == '__main__':
    print([3,3,3,1,2,1,1,2,3,3,4])
    
    print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
    print(totalFruit([1, 2, 1]))
    print(totalFruit([1,2,3,2,2]))
    print(totalFruit([0, 1, 1, 4, 3]))
    print(totalFruit([0, 1, 1]))
