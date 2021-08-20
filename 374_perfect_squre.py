

def my_sqrt(x):
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        if x == mid ** 2:
            return True
        elif mid ** 2 > x:
            right = mid - 1
        else:
            left = mid + 1
    return False

if __name__ == '__main__':
    print(my_sqrt(16))
    