

def spiralOrder(matrix):
    arr = list()
    n = len(matrix[0])
    m = len(matrix)
    up, down, left, right = 0, m-1, 0, n-1
    while True:
        # [1, 3) 从左到右
        for a in range(left, right+1):
            arr.append(matrix[up][a])
        # [3, 5) 从上到下
        up += 1
        if up > down:
            break
        for b in range(up, down+1):
            arr.append(matrix[b][right])
        right -= 1
        if right < left:
            break
        # [5, 7) 从右到左
        for c in range(right, left-1, -1):
            arr.append(matrix[down][c])
        down -= 1
        if down < up:
            break
        # [7, 9) 从下到上
        for d in range(down, up-1, -1):
            arr.append(matrix[d][left])
        left += 1
        if left > right:
            break
    return arr


if __name__ == '__main__':
    print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(spiralOrder([[1,2,3, 4],[5, 6, 7,8]]))
    print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    