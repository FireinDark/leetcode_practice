
def search(source, target):
    bottom = 0
    top = len(source) - 1
    while bottom <= top:
        mid = int((top + bottom) / 2)
        if target > source[mid]:
            bottom = mid + 1
        elif target < source[mid]:
            top = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    print(search([-1,0,3,5,9,12], 2))
    print(search([-1,0,3,5,9,12], 9))
    