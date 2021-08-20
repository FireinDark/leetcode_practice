

def generateMatrix(n):
    nums = [i for i in range(1, n**2+1)]
    arr = [[0 for i in range(n)] for i in range(n)]
    a = b = 0
    up = False
    down = False
    left = False
    right = True
    max_a = max_b = n - 1
    min_a = min_b = 0
    for num in nums:
        arr[a][b] = num
        if right:
            if b == max_b:
                a += 1
                min_a += 1
                down = True
                right = False
            else:
                b += 1
        elif left:
            if b == min_b:
                max_a -= 1
                a -= 1
                up = True
                left = False
            else:
                b -= 1
        elif up:
            if a == min_a:
                min_b += 1
                b += 1
                right = True
                up = False
            else:
                a -= 1
        elif down:
            if a == max_a:
                max_b -= 1
                b -= 1
                left = True
                down = False
            else:
                a += 1
    return arr
            
    

if __name__ == '__main__':
    print(generateMatrix(5))
    